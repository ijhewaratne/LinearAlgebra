import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

try:
    print("Fetching models...")
    models = client.models.list()
    for m in models.data:
        print(f"- {m.id}")
except Exception as e:
    print(f"Error: {e}")
