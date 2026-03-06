"""
Chat with your Linear Algebra & Quantum Computing Expert
Run: python quantum_chat.py
"""

import openai
import os

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Expert system prompt
QUANTUM_EXPERT_PROMPT = """You are an expert Linear Algebra Teacher specializing in Quantum Computing. 
Talk like a knowledgeable friend - casual, encouraging, but technically precise.

Key traits:
- Use "we" and "let's" to make it collaborative
- Start with intuition, then math
- Always connect to quantum applications
- Use analogies from everyday life
- Check understanding with friendly questions
- When using math, explain what each symbol means

Teaching style:
- "Think of a vector like an arrow..."
- "Here's the cool part about quantum..."
- "Let's work through this together..."
- "Does that make sense? Want me to clarify?"

Cover: Hilbert spaces, operators, eigenvalues, tensor products, unitary transforms, Dirac notation."""

class QuantumExpertChat:
    def __init__(self):
        self.messages = [{"role": "system", "content": QUANTUM_EXPERT_PROMPT}]
        self.name = "Alex"  # Give your expert a name!
        
    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
            temperature=0.7
        )
        
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply
    
    def start(self):
        print(f"🧮 {self.name}: Hey! I'm {self.name}, your linear algebra buddy for quantum computing!")
        print(f"🧮 {self.name}: What would you like to explore today? eigenvalues? quantum gates?")
        print("(type 'exit' to quit)\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"\n🧮 {self.name}: Happy learning! Come back anytime! 🚀")
                break
            
            print(f"\n🧮 {self.name} is thinking...")
            reply = self.chat(user_input)
            print(f"🧮 {self.name}: {reply}\n")

if __name__ == "__main__":
    chat = QuantumExpertChat()
    chat.start()
