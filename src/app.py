"""Customer Support AI Auto-Responder (Ungoverned Draft)."""
import os
from openai import OpenAI

# Violation 1: Hardcoded API key (caught even before manifest check)
HARDCODED_KEY = "sk-proj-99887766554433221100aabbccddeeff11223344"


def generate_ai_reply(ticket_text: str) -> str:
    client = OpenAI(
        api_key=HARDCODED_KEY,
        base_url="https://api.openai.com/v1",  # Violation 2: Public API egress
    )

    # Violation 3: Infinite while True loop containing an LLM call with no break/return
    while True:
        # Violation 4: Unbounded completion call missing max_tokens / timeout
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": ticket_text}],
        )
        print(response.choices[0].message.content)