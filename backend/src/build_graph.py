from langgraph.graph import StateGraph, START, END
from functools import lru_cache

from backend.src.nodes.memory_extraction_node import memory_extraction_node
from backend.src.nodes.memory_injection_node import memory_injection_node
from backend.src.nodes.context_injection_node import context_injection_node
from backend.src.nodes.router_node import router_node
from backend.src.nodes.audio_node import audio_node
from backend.src.nodes.image_node import image_node
from backend.src.nodes.conversation_node import conversation_node
from backend.src.nodes.summarize_conversation_node import summarize_conversation_node
from backend.src.graph_state import AIAgentState
from backend.src.edges.edges import should_summarize_conversation, select_workflow


@lru_cache(maxsize=1)
def build_graph():
    workflow = StateGraph(state_schema=AIAgentState)

    workflow.add_node("memory_extraction_node", memory_extraction_node)
    workflow.add_node("memory_injection_node", memory_injection_node)
    workflow.add_node("context_injection_node", context_injection_node)
    workflow.add_node("router_node", router_node)
    workflow.add_node("audio_node", audio_node)
    workflow.add_node("image_node", image_node)
    workflow.add_node("conversation_node", conversation_node)
    workflow.add_node("summarize_conversation_node", summarize_conversation_node)

    # First extract memories from user message
    workflow.add_edge(start_key=START, end_key="memory_extraction_node")

    # Then determine response type
    workflow.add_edge(start_key="memory_extraction_node", end_key="router_node")

    # Then inject both context and memories
    workflow.add_edge(start_key="router_node", end_key="context_injection_node")

    workflow.add_edge(start_key="context_injection_node", end_key="memory_injection_node")

    # Then proceed to appropriate response node
    workflow.add_conditional_edges("memory_injection_node", select_workflow)

    # Check for summarization after any response
    workflow.add_conditional_edges("conversation_node", should_summarize_conversation)

    workflow.add_conditional_edges("image_node", should_summarize_conversation)
    workflow.add_conditional_edges("audio_node", should_summarize_conversation)
    workflow.add_edge("summarize_conversation_node", END)

    return workflow


# Compiled without a checkpointer. Used for LangGraph Studio
build_graph().compile()



