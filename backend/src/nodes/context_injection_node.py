from src.graph_state import AIAgentState
from src.modules.schedules.context_generation import ScheduleContextGenerator


def context_injection_node(state: AIAgentState):
    """"""
    scheduler_context = ScheduleContextGenerator.get_current_activity()
    apply_activity = True if scheduler_context != state.get("current_activity", "") else False

    return {"apply_activity": apply_activity, "current_activity": scheduler_context}

