from langgraph.graph import END
from typing_extensions import Literal

from backend.src.graph_state import AIAgentState
from backend.src import settings


def select_workflow(state: AIAgentState) -> Literal["conversation_node", "image_node", "audio_node"]:
    workflow = state["workflow"]
    if workflow == "image":
        return "image_node"
    elif workflow == "audio":
        return "audio_node"
    else:
        return "conversation_node"


def should_summarize_conversation(state: AIAgentState) -> Literal["summarize_conversation_node", "__end__"]:
    messages = state["messages"]

    if len(messages) > settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "summarize_conversation_node"

    return END

