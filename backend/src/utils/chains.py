import os

from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import re

from src.core.prompts import CHARACTER_CARD_PROMPT, ROUTER_PROMPT
# from backend.src.settings import settings


def remove_asterisk_content(text: str) -> str:
    """Remove content between asterisks from the text."""
    return re.sub(r"\*.*?\*", "", text).strip()


class AsteriskRemovalParser(StrOutputParser):
    def parse(self, text):
        return remove_asterisk_content(super().parse(text))


class RouterResponse(BaseModel):
    response_type: str = Field(
        description="The response type to give to the user. It must be one of: 'conversation', 'image' or 'audio'"
    )


def get_chat_model(temperature: float = 0.7):
    return ChatGroq(
        model=os.getenv("TEXT_MODEL_NAME"),
        temperature=temperature,
    )


def get_router_chains():
    """"""
    model = get_chat_model(temperature=0.3).with_structured_output(RouterResponse)

    prompt = ChatPromptTemplate.from_messages([("system", ROUTER_PROMPT),
                                               MessagesPlaceholder(variable_name="messages")])

    return prompt | model


def get_character_response_chain(summary: str = ""):
    model = get_chat_model()
    system_prompt = CHARACTER_CARD_PROMPT

    if summary:
        system_prompt += f"\n\nSummary of conversation earlier between Ava and the user: {summary}"

    prompt = ChatPromptTemplate.from_messages(messages=[("system", system_prompt),
                                                        MessagesPlaceholder(variable_name="messages")])

    return prompt | model | AsteriskRemovalParser()



