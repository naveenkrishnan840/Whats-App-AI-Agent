import logging
import os
import uuid
from datetime import datetime
from typing_extensions import List, Optional

from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

from backend.src.core.prompts import MEMORY_ANALYSIS_PROMPT
from backend.src.modules.memory.long_term.vector_store import get_vector_store


class MemoryAnalysis(BaseModel):
    """Result of analyzing a message for memory-worthy content."""
    is_important: bool = (
        Field(..., description="Whether the message is important enough to be stored as a memory"))
    formatted_memory: Optional[str] = Field(..., description="The formatted memory to be stored")


class MemoryManager:
    def __init__(self):
        self.llm = ChatGroq(name=os.getenv("SMALL_TEXT_MODEL_NAME"),
                            temperature=0.2, max_retries=2).with_structured_output(MemoryAnalysis)
        self.logger = logging.getLogger(__name__)
        self.vector_store = get_vector_store()

    async def analyze_information(self, message: BaseMessage):
        """Analyze the information & important if needed."""
        prompt = MEMORY_ANALYSIS_PROMPT.format(message=message.content)
        return await self.llm.ainvoke(input=prompt)

    async def extract_store_information(self, message: BaseMessage):
        if message.type != "human":
            return

        analysis = await self.analyze_information(message=message)
        if analysis.is_important and analysis.formatted_memory:
            # check the similar message exists or not
            result = self.vector_store.find_similar_memories(analysis.formatted_memory)
            if result:
                # Skip storage if we already have a similar memory
                self.logger.info(
                    f"Similar memory already exists: '{analysis.formatted_memory}'"
                )
                return

            # Store new memory
            self.logger.info(f"Storing new memory: '{analysis.formatted_memory}'")

            self.vector_store.store_memory(query=analysis.formatted_memory,
                                           metadata={
                                               "id": str(uuid.uuid4()),
                                               "timestamp": datetime.now().isoformat()
                                           })

    def get_relevant_memories(self, content: str) -> List[str]:
        memories = self.vector_store.search_memory(query=content)
        if memories:
            for memory in memories:
                self.logger.debug(
                    f"Memory: '{memory.text}' (score: {memory.score:.2f})"
                )
        return [memory.text for memory in memories]

    def format_memories_for_prompt(self, memories: List[str]) -> str:
        """Format retrieved memories as bullet points."""
        if not memories:
            return ""
        return "\n".join(f"- {memory}" for memory in memories)


def get_memory_store() -> MemoryManager:
    """Get a MemoryManager instance."""
    return MemoryManager()
