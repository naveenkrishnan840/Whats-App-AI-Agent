import base64
import os
from pydantic import BaseModel, Field
from together import Together
from typing_extensions import Optional
from logging import getLogger
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder

# from src.settings import settings
from src.core.prompts import IMAGE_SCENARIO_PROMPT, IMAGE_ENHANCEMENT_PROMPT


class ScenarioPrompt(BaseModel):
    """Class for the scenario response"""
    narrative: str = Field(..., description="The AI's narrative response to the question")

    image_prompt: str = Field(..., description="The visual prompt to generate an image responding the scene")


class EnhancedPrompt(BaseModel):
    """Class for text prompt"""
    content: str = Field(description="The enhanced text prompt to generate an image")


class TextToImage:
    """A class to handle text-to-image generation using Together AI."""

    def __init__(self):
        self._together_client: Optional[Together] = None
        self.logger = getLogger(__name__)

    @property
    def together_client(self) -> Together:
        if not self._together_client:
            self._together_client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
        return self._together_client

    async def generate_image(self, prompt: str, output_path: str = "") -> bytes:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty")

        try:
            response = self.together_client.images.generate(prompt=prompt, model=os.getenv("TTI_MODEL_NAME"),
                                                            width=1024, height=768, steps=4, n=1,
                                                            response_format="b64_json")

            image_data = base64.b64decode(response.data[0].b64_json)

            if output_path:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                [os.remove(f"generated_images/{file}") for file in os.listdir("generated_images")]
                with open(file=output_path, mode="wb") as image:
                    image.write(image_data)
            self.logger.info(f"Image saved to {output_path}")
            return image_data
        except Exception as e:
            raise e

    async def create_scenario(self, chat_history: list = None) -> dict | BaseModel:
        """Creates a first-person narrative scenario and corresponding image prompt based on chat history."""
        try:
            formatted_query = "\n".join([f"{msg.type.title()}: {msg.content}" for msg in chat_history[-5:]])

            self.logger.info("Creating scenario from chat history")

            llm = ChatGroq(
                model=os.getenv("TEXT_MODEL_NAME"),
                temperature=0.4,
                max_retries=2,
            )
            structured_llm = llm.with_structured_output(ScenarioPrompt)
            chain = PromptTemplate(input_variables=["chat_history"], template=IMAGE_SCENARIO_PROMPT) | structured_llm
            scenario = chain.invoke(input={"chat_history": formatted_query})
            self.logger.info(f"Created scenario: {scenario}")
            return scenario

        except Exception as e:
            raise e

    async def enhance_prompt(self, prompt: str) -> str:
        """Enhance a simple prompt with additional details and context."""
        try:
            self.logger.info(f"Enhancing prompt: '{prompt}'")

            llm = ChatGroq(
                model=os.getenv("TEXT_MODEL_NAME"),
                temperature=0.25,
                max_retries=2,
            )

            structured_llm = llm.with_structured_output(EnhancedPrompt)

            chain = (
                PromptTemplate(
                    input_variables=["prompt"],
                    template=IMAGE_ENHANCEMENT_PROMPT,
                )
                | structured_llm
            )

            enhanced_prompt = chain.invoke({"prompt": prompt}).content
            self.logger.info(f"Enhanced prompt: '{enhanced_prompt}'")

            return enhanced_prompt

        except Exception as e:
            raise e


def get_text_to_image_module():
    return TextToImage()

