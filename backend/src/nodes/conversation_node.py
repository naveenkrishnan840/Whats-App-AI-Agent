from langchain_core.runnables import ensure_config
from langchain_core.messages import AIMessage

from backend.src.graph_state import AIAgentState
from backend.src.modules.schedules.context_generation import ScheduleContextGenerator
from backend.src.utils.chains import get_character_response_chain


async def conversation_node(state: AIAgentState):
    """"""
    schedule_context = ScheduleContextGenerator.get_current_activity()
    memory_context = state.get("memory_context", "")
    config = ensure_config()

    chain = get_character_response_chain(state.get("summary", ""))

    response = await chain.ainvoke(input={
        "messages": state["messages"],
        "current_activity": schedule_context,
        "memory_context": memory_context
    }, config=config)

    return {"messages": AIMessage(content=response)}


