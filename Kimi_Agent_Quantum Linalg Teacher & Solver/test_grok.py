import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

try:
    print("Testing non-stream...")
    response = client.chat.completions.create(
        model="grok-3",
        messages=[{"role": "user", "content": "What is 2+2?"}],
        temperature=0.7,
        stream=False
    )
    
    print(response)
    print("\nCONTENT:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
