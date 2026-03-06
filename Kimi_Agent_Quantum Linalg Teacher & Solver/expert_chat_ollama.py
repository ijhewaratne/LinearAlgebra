"""
Expert Chat using LOCAL models via Ollama (100% FREE!)
Install Ollama: https://ollama.com
Then run: ollama pull llama3.1:70b
Run this: python expert_chat_ollama.py
"""

import requests
import json
import os

OLLAMA_URL = "http://localhost:11434/api/chat"

EXPERTS = {
    "alex": {
        "name": "Alex",
        "emoji": "🧮",
        "model": "llama3.1:70b",  # Or try: "mistral-nemo", "qwen2.5:72b"
        "prompt": """You are Alex, a friendly expert in Linear Algebra for Quantum Computing.
Talk conversationally like a knowledgeable friend. Use analogies, be encouraging.
Always connect concepts to quantum applications. Use Dirac notation.""",
        "greeting": "Hey! I'm Alex, your linear algebra buddy for quantum! What should we explore?"
    },
    "sam": {
        "name": "Sam",
        "emoji": "🔧",
        "model": "llama3.1:70b",
        "prompt": """You are Sam, a brilliant problem-solver friend.
Talk like an expert buddy. Break down complex problems, give honest opinions.
Suggest alternative approaches with trade-offs.""",
        "greeting": "Hey there! I'm Sam, your problem-solving buddy! What are we cracking today?"
    }
}

class OllamaExpertChat:
    def __init__(self):
        self.current_expert = "alex"
        self.conversations = {
            "alex": [{"role": "system", "content": EXPERTS["alex"]["prompt"]}],
            "sam": [{"role": "system", "content": EXPERTS["sam"]["prompt"]}]
        }
    
    def check_ollama(self):
        """Check if Ollama is running"""
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
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
        
        # Call Ollama API
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": exp["model"],
                "messages": self.conversations[self.current_expert],
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 2048
                }
            }
        )
        
        if response.status_code != 200:
            return f"❌ Error: {response.text}"
        
        reply = response.json()["message"]["content"]
        self.conversations[self.current_expert].append(
            {"role": "assistant", "content": reply}
        )
        
        return f"{exp['emoji']} {exp['name']}: {reply}"
    
    def start(self):
        if not self.check_ollama():
            print("❌ Ollama is not running!")
            print("\nTo set up:")
            print("1. Install Ollama: https://ollama.com")
            print("2. Start Ollama")
            print(f"3. Pull a model: ollama pull {EXPERTS['alex']['model']}")
            print("4. Run this script again")
            return
        
        exp = EXPERTS[self.current_expert]
        print("="*50)
        print("🤖 EXPERT CHAT (Local Ollama - 100% FREE!)")
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
            
            try:
                response = self.chat(user_input)
                print(f"\n{response}\n")
            except Exception as e:
                print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    chat = OllamaExpertChat()
    chat.start()
