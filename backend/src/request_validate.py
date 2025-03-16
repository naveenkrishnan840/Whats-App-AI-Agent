from pydantic import BaseModel


class SignUpLogin(BaseModel):
    name: str
    phone_no: str


class ChatInput(BaseModel):
    chat_type: str
    user_text_input: str

