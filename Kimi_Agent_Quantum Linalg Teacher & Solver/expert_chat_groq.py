"""
Expert Chat using Groq's FREE API (1.5M tokens/day!)
Sign up: https://console.groq.com
Run: python expert_chat_groq.py
"""

import os
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

EXPERTS = {
    "alex": {
        "name": "Alex",
        "emoji": "🧮",
        "model": "llama3-70b-8192",  # Llama 3 70B - excellent for math!
        "prompt": """You are Alex, a friendly expert in Linear Algebra for Quantum Computing.
Talk conversationally like a knowledgeable friend. Use analogies, be encouraging.
Always connect concepts to quantum applications. Use Dirac notation.""",
        "greeting": "Hey! I'm Alex, your linear algebra buddy for quantum! What should we explore?"
    },
    "sam": {
        "name": "Sam",
        "emoji": "🔧",
        "model": "llama3-70b-8192",
        "prompt": """You are Sam, a brilliant problem-solver friend.
Talk like an expert buddy. Break down complex problems, give honest opinions.
Suggest alternative approaches with trade-offs.""",
        "greeting": "Hey there! I'm Sam, your problem-solving buddy! What are we cracking today?"
    }
}

class GroqExpertChat:
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
        if user_input.lower().startswith("switch to "):
            new_expert = user_input.lower().replace("switch to ", "").strip()
            return self.switch_expert(new_expert)
        
        self.conversations[self.current_expert].append(
            {"role": "user", "content": user_input}
        )
        
        exp = EXPERTS[self.current_expert]
        
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=self.conversations[self.current_expert],
            model=exp["model"],
            temperature=0.7,
            max_tokens=2048
        )
        
        reply = chat_completion.choices[0].message.content
        self.conversations[self.current_expert].append(
            {"role": "assistant", "content": reply}
        )
        
        return f"{exp['emoji']} {exp['name']}: {reply}"
    
    def start(self):
        exp = EXPERTS[self.current_expert]
        print("="*50)
        print("🤖 EXPERT CHAT (Powered by Groq - FREE!)")
        print("="*50)
        print(f"\n{exp['emoji']} {exp['name']}: {exp['greeting']}")
        print("\nCommands:")
        print("  'switch to alex' - Linear Algebra expert")
        print("  'switch to sam'  - Problem Solver")
        print("  'exit'           - Quit")
        print("-"*50 + "\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Goodbye! Happy learning! 🚀")
                break
            
            response = self.chat(user_input)
            print(f"\n{response}\n")

if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Please set GROQ_API_KEY environment variable")
        print("Get your free key at: https://console.groq.com")
        exit(1)
    
    chat = GroqExpertChat()
    chat.start()
