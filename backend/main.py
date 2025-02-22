import os
from io import BytesIO

from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Dict
import httpx
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from langgraph.checkpoint.duckdb.aio import AsyncDuckDBSaver
from langchain_core.messages import HumanMessage
from logging import getLogger

from backend.src.modules.speechs.speech_to_text import SpeechToText
from backend.src.modules.image.image_to_text import ImageToText
from backend.src import settings
from backend.src.build_graph import build_graph

app = FastAPI(title="What's App AI Agent")

logger = getLogger(__name__)
# app.add_middleware()

api_router = APIRouter()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


# Declare the Global Instance
speech_to_text = SpeechToText()
image_to_text = ImageToText()


@api_router.api_route(path="/whatapp-response", methods=["GET", "POST"])
async def whatapp_handler(request: Request) -> Response:
    """Handles incoming messages and status updates from the WhatsApp Cloud API."""
    if request.method == "GET":
        params = request.query_params
        if params.get("hub.verify_token") == os.getenv("WHATSAPP_VERIFY_TOKEN"):
            return Response(content=params.get("hub.challenge"), status_code=200)
        return Response(content="Verification token mismatch", status_code=403)

    try:
        data = await request.json()
        change_value = data["entry"][0]["changes"][0]["value"]
        if "messages" in change_value:
            message = change_value["messages"][0]
            from_number = message["from"]
            session_id = from_number

            # Get user message and handle different message types
            content = ""
            if message["type"] == "audio":
                content = await process_audio_message(message)
            # Get image caption if any
            elif message["type"] == "image":
                content = message.get("image", {}).get("caption", "")
                # Download image for your request message content
                image_bytes = await download_media(message["image"]["id"])
                try:
                    description = await image_to_text.analyze_image(
                        image_data=image_bytes,
                        prompt="Please describe what you see in this image in the context of our conversation.")
                    content += f"\n[Image Analysis: {description}]"
                except Exception as e:
                    raise e
            else:
                content = message["text"]["body"]
            with AsyncSqliteSaver.from_conn_string(conn_string=settings.SHORT_TERM_MEMORY_DB_PATH) as checkpointer:
                graph = build_graph.compile(checkpointer=checkpointer)
                await graph.ainvoke(input={
                    "messages": HumanMessage(content=content)},
                    config={"configurable": {"thread_id": session_id}})

                # Get the workflow type and response from the state
                output_state = await graph.aget_state(config={"configurable": {"thread_id": session_id}})

                workflow = output_state.values.get("workflow", "conversation")
                response_message = output_state.values["messages"][-1].content

                if workflow == "audio":
                    audio_buffer = output_state.values.get("audio_buffer")
                    success = await send_response()
        elif "statuses" in change_value:
            return Response(content="Status update received", status_code=200)
        else:
            return Response(content="unknown event type", status_code=400)

    except Exception as e:
        raise e


async def process_audio_message(message: Dict) -> str:
    """Download and transcribe audio message."""
    audio_id = message["audio"]["id"]
    media_metadata_url = f"https://graph.facebook.com/v21.0/{audio_id}"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    with httpx.AsyncClient() as client:
        metadata_response = await client.get(media_metadata_url, headers)
        metadata_response.raise_for_status()
        metadata = metadata_response.json()
        download_url = metadata.get("url")
        audio_response = client.get(download_url, headers)
        audio_response.raise_for_status()

    audio_content = BytesIO(audio_response.content)
    audio_content.seek(0)
    audio_data = audio_content.read()

    return await speech_to_text.transcribe(audio_data=audio_data)


async def download_media(media_id: str) -> bytes:
    """Download media from WhatsApp."""
    media_metadata_url = f"https://graph.facebook.com/v21.0/{media_id}"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}

    with httpx.AsyncClient() as client:
        metadata_response = client.get(media_metadata_url, headers)
        metadata_response.raise_for_status()
        metadata = metadata_response.json()
        media_response = await client.get(metadata.get("url"), headers)
        media_response.raise_for_status()
        return media_response.content


async def send_response(from_number: str, response_text: str, message_type: str = "text", media_content: bytes = None):
    """Send response to user via WhatsApp API."""
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    if message_type in ["audio", "image"]:
        try:
            mime_type = "audio/mpeg" if message_type == "audio" else "image/png"
            media_buffer = BytesIO(media_content)
            media_id = await upload_media(media_content=media_buffer, mime_type=mime_type)
            json_data = {
                "messaging_product": "whatsapp",
                "to": from_number,
                "type": message_type,
                message_type: {"id": media_id},
            }
            # Add caption for images
            if message_type == "image":
                json_data["image"]["caption"] = response_text
        except Exception as e:
            logger.error(f"Media upload failed, falling back to text: {e}")
            message_type = "text"

        if message_type == "text":
            json_data = {
                "messaging_product": "whatsapp",
                "to": from_number,
                "type": "text",
                "text": {"body": response_text},
            }

        print(headers)
        print(json_data)

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://graph.facebook.com/v21.0/{WHATSAPP_PHONE_NUMBER_ID}/messages",
                headers=headers,
                json=json_data,
            )
        return response.status_code == 200


async def upload_media(media_content: BytesIO, mime_type: str) -> str:
    """Upload media to WhatsApp servers."""
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    files = {"file": ("response.mp3", media_content, mime_type)}
    data = {"messaging_product": "whatsapp", "type": mime_type}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://graph.facebook.com/v21.0/{WHATSAPP_PHONE_NUMBER_ID}/media",
            headers=headers,
            files=files,
            data=data,
        )
        result = response.json()

    if "id" not in result:
        raise Exception("Failed to upload media")
    return result["id"]


app.include_router(router=api_router)

