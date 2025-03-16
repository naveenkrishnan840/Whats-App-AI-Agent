import os

from langchain_core.messages import HumanMessage, RemoveMessage

from backend.src.graph_state import AIAgentState
from backend.src.utils.chains import get_chat_model
from backend.src.settings import settings


async def summarize_conversation_node(state: AIAgentState):
    model = get_chat_model()
    summary = state.get("summary", "")

    if summary:
        summary_message = (
            f"This is summary of the conversation to date between Ava and the user: {summary}\n\n"
            "Extend the summary by taking into account the new messages above:"
        )
    else:
        summary_message = (
            "Create a summary of the conversation above between Ava and the user. "
            "The summary must be a short description of the conversation so far, "
            "but that captures all the relevant information shared between Ava and the user:"
        )

    messages = state["messages"] + [HumanMessage(content=summary_message)]
    response = await model.ainvoke(messages)

    delete_messages = [
        RemoveMessage(id=m.id)
        for m in state["messages"][: - int(os.getenv("TOTAL_MESSAGES_AFTER_SUMMARY"))]
    ]
    return {"summary": response.content, "messages": delete_messages}
