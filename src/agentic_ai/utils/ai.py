import asyncio
from ollama import AsyncClient

async def chat(cateogry: str, available_actions: list[str], user_prompt: str) -> str:
    """
    Send A Query to Qwen3 600M Model and get back the results.
    """
    response = await AsyncClient().chat(
        model="qwen3:0.6b",
        messages=[
            {
                "role": "system",
                "content": f"Respond using plain text only. Markdown is strictly prohibited. You are an{cateogry} robot and here the actions {available_actions} do what the user is telling you to do."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.message.content

print(asyncio.run(chat()))