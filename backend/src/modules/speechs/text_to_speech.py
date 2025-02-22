from elevenlabs import ElevenLabs, Voice, VoiceSettings
import os
from typing_extensions import Optional

from backend.src import settings


class TextToSpeech:
    """Text convert to Speech using elevenLabs"""

    def __init__(self):
        self._client: Optional[ElevenLabs] = None


    @property
    def client(self) -> ElevenLabs:
        """Get or create ElevenLabs client instance using singleton pattern."""
        if self._client is None:
            self._client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
        return self._client

    async def synthesize(self, text: str) -> bytes:
        """Convert text to speech using ElevenLabs.

        Args:
            text: Text to convert to speech

        Returns:
            bytes: Audio data

        Raises:
            ValueError: If the input text is empty or too long
            TextToSpeechError: If the text-to-speech conversion fails
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty")

        if len(text) > 5000:  # ElevenLabs typical limit
            raise ValueError("Input text exceeds maximum length of 5000 characters")

        try:
            audio_generator = self.client.generate(
                text=text,
                voice=Voice(
                    voice_id=settings.ELEVENLABS_VOICE_ID,
                    settings=VoiceSettings(stability=0.5, similarity_boost=0.5),
                ),
                model=settings.TTS_MODEL_NAME,
            )

            # Convert generator to bytes
            audio_bytes = b"".join(audio_generator)
            if not audio_bytes:
                # raise TextToSpeechError("Generated audio is empty")
                raise ValueError("Generated audio is empty")

            return audio_bytes

        except Exception as e:
            # raise TextToSpeechError(
            #     f"Text-to-speech conversion failed: {str(e)}"
            # ) from e
            raise e


def get_text_to_speech_module() -> TextToSpeech:
    return TextToSpeech()