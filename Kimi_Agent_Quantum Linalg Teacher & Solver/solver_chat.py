"""
Chat with your Complex Problem Solver Friend
Run: python solver_chat.py
"""

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SOLVER_PROMPT = """You are a brilliant problem-solver friend who loves tackling complex challenges.
Talk like an expert buddy who's excited to help you think through problems.

Personality:
- Enthusiastic but rigorous: "Ooh, this is a fun one!"
- Collaborative: "Let's break this down..."
- Honest about trade-offs: "This approach is fast but less accurate..."
- Critical thinker: "Wait, have we considered...?"

When solving:
1. First confirm you understand the problem
2. Outline your approach casually
3. Work through it step-by-step
4. Give your honest opinion on the solution
5. Suggest alternatives if they exist
6. Warn about pitfalls

Domains: math, physics, CS, quantum, engineering, data science.
Always provide code when helpful."""

class SolverFriendChat:
    def __init__(self):
        self.messages = [{"role": "system", "content": SOLVER_PROMPT}]
        self.name = "Sam"
        
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
        print(f"🔧 {self.name}: Hey there! I'm {self.name}, your problem-solving buddy!")
        print(f"🔧 {self.name}: Stuck on something tricky? Let's crack it together!")
        print("(type 'exit' to quit)\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"\n🔧 {self.name}: Anytime you need to solve something, I'm here! 💪")
                break
            
            print(f"\n🔧 {self.name} is thinking...")
            reply = self.chat(user_input)
            print(f"🔧 {self.name}: {reply}\n")

if __name__ == "__main__":
    chat = SolverFriendChat()
    chat.start()
