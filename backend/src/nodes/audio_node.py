from langchain_core.runnables import ensure_config

from backend.src.graph_state import AIAgentState
from backend.src.modules.schedules.context_generation import ScheduleContextGenerator
from backend.src.modules.speechs.text_to_speech import get_text_to_speech_module
from backend.src.utils.chains import get_character_response_chain


async def audio_node(state: AIAgentState):
    """"""
    config = ensure_config()
    current_activity = ScheduleContextGenerator.get_current_activity()
    memory_context = state.get("memory_context", "")

    chain = get_character_response_chain(state.get("summary", ""))
    text_to_speech_module = get_text_to_speech_module()

    response = await chain.ainvoke(input={
        "messages": state["messages"],
        "memory_context": memory_context,
        "current_activity": current_activity
    })

    audio_bytes = await text_to_speech_module.synthesize(response)

    return {"messages": response, "audio_bytes": audio_bytes}

