import dataclasses
import os

from typing_extensions import Optional, List
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from datetime import datetime

from backend.src.settings import settings


@dataclasses.dataclass
class Memory:
    """Represents a memory entry in the vector store."""

    text: str
    metadata: dict
    score: Optional[float] = None

    @property
    def id(self) -> Optional[str]:
        return self.metadata.get("id")

    @property
    def timestamp(self) -> Optional[datetime]:
        ts = self.metadata.get("timestamp")
        return datetime.fromisoformat(ts) if ts else None


class VectorStore:
    SENTENCE_TRANSFORMERS_NAME = "all-MiniLM-L6-v2"
    COLLECTION_NAME = "long_term_memory"
    SIMILARITY_THRESHOLD = 0.9  # Threshold for considering memories as similar
    _instance: Optional["VectorStore"] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.embedding_model = SentenceTransformer(model_name_or_path=self.SENTENCE_TRANSFORMERS_NAME)
            self.client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"),
                                       check_compatibility=False)
            self._initialized = True
            if not self.check_client_collections():
                self.create_collections()

    def check_client_collections(self):
        """Check if the memory collection exists."""
        collections = self.client.get_collections().collections
        return any([col.name == self.COLLECTION_NAME for col in collections])

    def create_collections(self):
        """To create new memory collections"""
        sample_embedding = self.embedding_model.encode("sample text")
        self.client.create_collection(collection_name=self.COLLECTION_NAME,
                                      vectors_config=VectorParams(size=len(sample_embedding), distance=Distance.COSINE))

    def search_memory(self, query: str, k: int = 5) -> List[Memory]:
        """
        Search for similar memories in the vector store.
        :param query:
        :param k:
        :return: List of the Memory Objects
        """
        # if self.check_client_collections():
        #     return []
        query_vector = self.embedding_model.encode(sentences=query)
        results = self.client.query_points(collection_name=self.COLLECTION_NAME, query=query_vector, limit=k)

        return ([Memory(text=hit.payload["text"],
                        metadata={k: v for k, v in hit.payload.items() if k != "text"}, score=hit.score)
                 for hit in results.points])

    def find_similar_memories(self, text: str) -> Optional[Memory]:
        """

        :return:
        """
        result = self.search_memory(query=text, k=1)
        if result and result[0].score >= self.SIMILARITY_THRESHOLD:
            return result[0]
        return None

    def store_memory(self, query: str, metadata: dict) -> None:
        """
        Store a new memory in the vector store or update if similar exists.
        :param query:
        :param metadata:
        :return:
        """

        memories_ids = self.find_similar_memories(text=query)
        if memories_ids and memories_ids.id:
            metadata["id"] = memories_ids.id

        inputs = self.embedding_model.encode(sentences=query)

        point = PointStruct(id=metadata.get("id", hash(query)), vector=inputs.tolist(), payload={"text": query, **metadata})

        self.client.upsert(collection_name=self.COLLECTION_NAME, points=[point])


def get_vector_store() -> VectorStore:
    """get recent conversation or else store conversation"""
    return VectorStore()
