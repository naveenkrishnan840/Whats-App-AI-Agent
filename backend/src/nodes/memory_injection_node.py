from backend.src.modules.memory.long_term.memory_manager import get_memory_store
from backend.src.graph_state import AIAgentState


def memory_injection_node(state: AIAgentState):
    """Retrieve the inject the memories into character card"""
    memory = get_memory_store()

    # Get Relevant memories from vector store
    content = " ".join([message.content for message in state["messages"][-3:]])
    memories = memory.get_relevant_memories(content=content)

    # Format memories for the character card
    memory_context = memory.format_memories_for_prompt(memories=memories)

    return {"memory_context": memory_context}

