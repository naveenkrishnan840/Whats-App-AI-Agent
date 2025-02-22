import os
import tempfile
from typing_extensions import Optional
from groq import Groq

from backend.src import settings


class SpeechToText:

    def __init__(self):
        self._client: Optional[Groq] = None

    @property
    def client(self) -> Groq:
        """Get or create Groq client instance using singleton pattern."""
        if self._client is None:
            self._client = Groq(api_key=settings.GROQ_API_KEY)
        return self._client

    def transcribe(self, audio_data: bytes):
        """Convert speech to text using Groq's Whisper model.

        Args:
            audio_data: Binary audio data

        Returns:
            str: Transcribed text

        Raises:
            ValueError: If the audio file is empty or invalid
            RuntimeError: If the transcription fails
        """
        if not audio_data:
            raise ValueError("Audio data cannot be empty")
        try:
            with tempfile.TemporaryFile(suffix=".wav", delete=False) as temp_file:
                temp_file.write(audio_data)
                temp_file_path = temp_file.name
            try:
                with open(temp_file_path, "rb") as file:
                    transcription = self._client.audio.transcriptions.create(file=file, model="whisper-large-v3-turbo",
                                                                             language="en", response_format="text")

                    if transcription:
                        raise ValueError("Transcription result is empty")

                return transcription
            finally:
                os.unlink(path=temp_file_path)
        except Exception as e:
            raise e
