"""
Unified Expert Chat - Talk to both experts! (Terminal Version)
Run: python unified_expert_chat.py
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load keys from .env
load_dotenv()

# Initialize Grok Client
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

EXPERTS = {
    "alex": {
        "name": "Alex",
        "emoji": "🧮",
        "prompt": """You are Alex, a friendly expert in Linear Algebra for Quantum Computing.
        Talk like a knowledgeable friend. Use casual language but be technically precise.
        Always connect concepts to quantum applications. Use analogies. Check understanding.""",
        "greeting": "Hey! I'm Alex, your linear algebra buddy for quantum! What should we explore?"
    },
    "sam": {
        "name": "Sam", 
        "emoji": "🔧",
        "prompt": """You are Sam, a brilliant problem-solver friend.
        Talk like an expert buddy. Be enthusiastic but rigorous.
        Break down complex problems. Give honest opinions. Suggest alternatives.""",
        "greeting": "Hey there! I'm Sam, your problem-solving buddy! What are we cracking today?"
    }
}

class UnifiedExpertChat:
    def __init__(self):
        self.current_expert = "alex"
        self.conversations = {
            "alex": [{"role": "system", "content": EXPERTS["alex"]["prompt"]}],
            "sam": [{"role": "system", "content": EXPERTS["sam"]["prompt"]}]
        }
    
    def switch_expert(self, expert_key):
        if expert_key in EXPERTS:
            self.current_expert = expert_key
            exp = EXPERTS[expert_key]
            print(f"\n{'='*50}")
            print(f"Switched to {exp['emoji']} {exp['name']}")
            print(f"{'='*50}\n")
            return f"{exp['emoji']} {exp['name']}: {exp['greeting']}"
        return "Unknown expert. Choose 'alex' or 'sam'"
    
    def chat(self, user_input):
        # Check for switch command
        if user_input.lower().startswith("switch to "):
            new_expert = user_input.lower().replace("switch to ", "").strip()
            return self.switch_expert(new_expert)
        
        # Add user message
        self.conversations[self.current_expert].append(
            {"role": "user", "content": user_input}
        )
        
        # Get response from Grok
        try:
            response = client.chat.completions.create(
                model="grok-3",
                messages=self.conversations[self.current_expert],
                temperature=0.7
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"❌ API Error: {str(e)}"
            
        self.conversations[self.current_expert].append(
            {"role": "assistant", "content": reply}
        )
        
        exp = EXPERTS[self.current_expert]
        return f"{exp['emoji']} {exp['name']}: {reply}"
    
    def start(self):
        exp = EXPERTS[self.current_expert]
        print("="*50)
        print("🤖 UNIFIED EXPERT CHAT")
        print("="*50)
        print(f"\n{exp['emoji']} {exp['name']}: {exp['greeting']}")
        print("\nCommands:")
        print("  'switch to alex' - Talk to Linear Algebra expert")
        print("  'switch to sam'  - Talk to Problem Solver")
        print("  'exit'           - Quit")
        print("-"*50 + "\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Goodbye! Happy learning and problem solving! 🚀")
                break
            
            response = self.chat(user_input)
            print(f"\n{response}\n")

if __name__ == "__main__":
    chat = UnifiedExpertChat()
    chat.start()
