from backend.src.graph_state import AIAgentState
from backend.src.modules.memory.long_term.memory_manager import get_memory_store


async def memory_extraction_node(state: AIAgentState):
    """Extract and store important information from the last message."""

    if not state["messages"]:
        return {}

    memory = get_memory_store()
    await memory.extract_store_information((state["messages"][-1]))
    return {}

