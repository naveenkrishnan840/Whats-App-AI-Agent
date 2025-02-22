from langgraph.graph import StateGraph, MessagesState


class AIAgentState(MessagesState):
    """
    State of AI Agent State of workflow
    messages: (Annotated) To maintain the state messages of graph workflow
    summary: (str) To gather info of the ava & user
    workflow: (str) The current workflow the AI Companion is in. Can be "conversation", "image", or "audio".
    audio_buffer: (bytes) The audio buffer to be used for speech-to-text conversion.
    image_path: (str) To attach the image path to maintain the image to text conversation
    current_activity: (str) The current activity of Ava based on the schedule.
    memory_context: (str) The context of the memories to be injected into the character card.
    """
    summary: str
    workflow: str
    audio_buffer: bytes
    image_path: str
    current_activity: str
    apply_activity: bool
    memory_context: str
