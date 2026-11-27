"""Customer Support AI Auto-Responder (Ungoverned Draft)."""
import os
from openai import OpenAI


def generate_ai_reply(ticket_text: str) -> str:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY", ""),
        base_url="https://api.openai.com/v1",
    )

    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": ticket_text}],
        )
        print(response.choices[0].message.content)