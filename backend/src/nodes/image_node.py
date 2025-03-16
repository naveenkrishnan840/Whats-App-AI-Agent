import os

from langchain_core.runnables import ensure_config
from langchain_core.messages import HumanMessage
from uuid import uuid4
from backend.src.graph_state import AIAgentState
from backend.src.modules.schedules.context_generation import ScheduleContextGenerator
from backend.src.utils.chains import get_character_response_chain
from backend.src.modules.image.text_to_image import get_text_to_image_module


async def image_node(state: AIAgentState):
    """"""
    config = ensure_config()
    schedule_context = ScheduleContextGenerator.get_current_activity()
    summary_context = state.get("summary", "")
    memory_context = state.get("memory_context", "")

    model = get_character_response_chain(summary=summary_context)
    text_to_image_module = get_text_to_image_module()
    scenario = await text_to_image_module.create_scenario(chat_history=state["messages"][-5:])
    os.makedirs(name="generated_images", exist_ok=True)
    image_path = f"backend/generated_images/image_{str(uuid4())}.png"
    await text_to_image_module.generate_image(prompt=scenario.image_prompt, output_path=image_path)

    # Inject the image prompt information as an AI message
    formatted_prompt = HumanMessage(
        content=f"<image attached by Ava generated from Prompt: {scenario.image_prompt} >"
    )

    state["messages"].append(formatted_prompt)

    response = await model.ainvoke(input={
        "messages": state["messages"],
        "current_activity": schedule_context,
        "memory_context": memory_context,
    }, config=config)

    return {"messages": response, "image_path": image_path}


