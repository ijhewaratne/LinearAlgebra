"""
Universal Expert Chat - Uses best available FREE option
Auto-detects: Groq → Ollama → Other free APIs
Run: python expert_chat_universal.py
"""

import os
import sys
import requests

# Try to import different clients
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

class UniversalExpertChat:
    """Automatically uses best available free LLM backend"""
    
    def __init__(self):
        self.backend = None
        self.client = None
        self.ollama_url = "http://localhost:11434/api/chat"
        
        # Expert configurations
        self.experts = {
            "alex": {
                "name": "Alex",
                "emoji": "🧮",
                "prompt": """You are Alex, a friendly expert in Linear Algebra for Quantum Computing.
Talk conversationally like a knowledgeable friend. Use analogies, be encouraging.
Always connect concepts to quantum applications. Use Dirac notation.""",
                "greeting": "Hey! I'm Alex, your linear algebra buddy for quantum! What should we explore?"
            },
            "sam": {
                "name": "Sam",
                "emoji": "🔧",
                "prompt": """You are Sam, a brilliant problem-solver friend.
Talk like an expert buddy. Break down complex problems, give honest opinions.
Suggest alternative approaches with trade-offs.""",
                "greeting": "Hey there! I'm Sam, your problem-solving buddy! What are we cracking today?"
            }
        }
        
        self.current_expert = "alex"
        self.conversations = {
            "alex": [{"role": "system", "content": self.experts["alex"]["prompt"]}],
            "sam": [{"role": "system", "content": self.experts["sam"]["prompt"]}]
        }
        
        self._detect_backend()
    
    def _detect_backend(self):
        """Auto-detect best available backend"""
        print("🔍 Detecting available LLM backends...\n")
        
        # Check 1: Groq (best free API)
        groq_key = os.getenv("GROQ_API_KEY")
        if GROQ_AVAILABLE and groq_key:
            try:
                client = Groq(api_key=groq_key)
                # Test API
                client.chat.completions.create(
                    messages=[{"role": "user", "content": "test"}],
                    model="llama3-8b-8192",
                    max_tokens=5
                )
                self.backend = "groq"
                self.client = client
                print("✅ Using Groq API (1.5M free tokens/day)")
                return
            except Exception as e:
                print(f"⚠️  Groq key found but API test failed: {e}")
        elif groq_key and not GROQ_AVAILABLE:
            print("⚠️  GROQ_API_KEY found but 'groq' package not installed")
            print("    Run: pip install groq")
        else:
            print("⚠️  No GROQ_API_KEY found")
        
        # Check 2: Ollama (local)
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=3)
            if response.status_code == 200:
                models = response.json().get("models", [])
                if models:
                    self.backend = "ollama"
                    # Find best available model
                    model_names = [m["name"] for m in models]
                    print(f"✅ Using Ollama (local)")
                    print(f"   Available models: {', '.join(model_names)}")
                    
                    # Choose best model
                    if "llama3.1:70b" in model_names:
                        self.ollama_model = "llama3.1:70b"
                    elif "llama3.1:8b" in model_names:
                        self.ollama_model = "llama3.1:8b"
                    elif "mistral-nemo" in model_names:
                        self.ollama_model = "mistral-nemo"
                    else:
                        self.ollama_model = model_names[0]
                    print(f"   Using: {self.ollama_model}")
                    return
                else:
                    print("⚠️  Ollama running but no models downloaded")
                    print("    Run: ollama pull llama3.1:8b")
        except:
            print("⚠️  Ollama not running")
        
        # No backend found
        print("\n" + "="*60)
        print("❌ NO LLM BACKEND FOUND")
        print("="*60)
        print("\nTo use this chat, you need ONE of:")
        print("\n1. Groq API (easiest, recommended):")
        print("   - Get free key: https://console.groq.com")
        print("   - export GROQ_API_KEY='your-key'")
        print("   - pip install groq")
        print("\n2. Ollama (local, private):")
        print("   - Install: https://ollama.com")
        print("   - ollama pull llama3.1:8b")
        print("\n" + "="*60)
        sys.exit(1)
    
    def _call_groq(self, messages):
        """Call Groq API"""
        model = "llama3-70b-8192"  # Best quality
        response = self.client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=0.7,
            max_tokens=2048
        )
        return response.choices[0].message.content
    
    def _call_ollama(self, messages):
        """Call Ollama API"""
        response = requests.post(
            self.ollama_url,
            json={
                "model": self.ollama_model,
                "messages": messages,
                "stream": False,
                "options": {"temperature": 0.7, "num_predict": 2048}
            }
        )
        return response.json()["message"]["content"]
    
    def get_response(self, user_input):
        """Get response from current backend"""
        self.conversations[self.current_expert].append(
            {"role": "user", "content": user_input}
        )
        
        if self.backend == "groq":
            reply = self._call_groq(self.conversations[self.current_expert])
        elif self.backend == "ollama":
            reply = self._call_ollama(self.conversations[self.current_expert])
        else:
            return "Error: No backend available"
        
        self.conversations[self.current_expert].append(
            {"role": "assistant", "content": reply}
        )
        
        exp = self.experts[self.current_expert]
        return f"{exp['emoji']} {exp['name']}: {reply}"
    
    def switch_expert(self, expert_key):
        if expert_key in self.experts:
            self.current_expert = expert_key
            exp = self.experts[expert_key]
            print(f"\n{'='*50}")
            print(f"Switched to {exp['emoji']} {exp['name']}")
            print(f"{'='*50}\n")
            return f"{exp['emoji']} {exp['name']}: {exp['greeting']}"
        return "Unknown expert. Choose 'alex' or 'sam'"
    
    def chat(self, user_input):
        if user_input.lower().startswith("switch to "):
            new_expert = user_input.lower().replace("switch to ", "").strip()
            return self.switch_expert(new_expert)
        return self.get_response(user_input)
    
    def start(self):
        exp = self.experts[self.current_expert]
        print("\n" + "="*50)
        print("🤖 UNIVERSAL EXPERT CHAT")
        print(f"Backend: {self.backend.upper()}")
        print("="*50)
        print(f"\n{exp['emoji']} {exp['name']}: {exp['greeting']}")
        print("\nCommands:")
        print("  'switch to alex' - Linear Algebra expert")
        print("  'switch to sam'  - Problem Solver")
        print("  'exit'           - Quit")
        print("-"*50 + "\n")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\n👋 Goodbye! Happy learning! 🚀")
                    break
                
                response = self.chat(user_input)
                print(f"\n{response}\n")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    chat = UniversalExpertChat()
    chat.start()
