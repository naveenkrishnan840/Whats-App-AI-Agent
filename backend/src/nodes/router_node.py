import os

from backend.src.graph_state import AIAgentState
from backend.src.utils.chains import get_router_chains
from backend.src.settings import settings


async def router_node(state: AIAgentState):
    """To decide the workflow, which to choose to go"""

    chains = get_router_chains()

    response = await chains.ainvoke(input=state["messages"][- int(os.getenv("ROUTER_MESSAGES_TO_ANALYZE")):])

    return {"workflow": response.response_type}
