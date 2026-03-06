# 🤖 Expert Chat - Linear Algebra & Problem Solving

Chat with AI experts like they're your friends! Two personalities:
- **🧮 Alex** - Linear Algebra & Quantum Computing expert
- **🔧 Sam** - Complex Problem Solver

## 🚀 Quick Start

### 1. Set your OpenAI API key
```bash
export OPENAI_API_KEY="your-key-here"
```

Or create a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

### 2. Choose your interface

#### Option A: Terminal Chat (Simplest)
```bash
# Talk to Alex (Linear Algebra)
python quantum_chat.py

# Talk to Sam (Problem Solver)
python solver_chat.py

# Talk to both (switch anytime)
python unified_expert_chat.py
```

#### Option B: Web App (Prettiest & Most Featured)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run expert_chat_app.py
```
Then open http://localhost:8501 in your browser.

**Features in Web App:**
- Dropdown to select your AI backend: **Ollama (Local & Free)**, **Grok (xAI)**, **OpenAI**, or **Groq**.
- Simply select your provider, enter the API key (or model name for Ollama), and start chatting!

## 💬 Example Conversations

### With Alex (🧮)
```
You: Hey Alex, what's a tensor product and why does it matter in quantum?
Alex: Hey! Great question! Think of it like this...

You: Can you show me how to write a CNOT gate as a matrix?
Alex: Absolutely! Let's build it together...

You: I'm struggling with understanding Hermitian operators
Alex: No worries, let's break it down...
```

### With Sam (🔧)
```
You: Sam, I need to optimize this function, what approach should I use?
Sam: Ooh, fun! Let's look at what you're dealing with...

You: Is gradient descent the best choice here?
Sam: Good question! It depends on a few things...

You: Solve this system of equations and tell me if there's a better way
Sam: Let's see... Actually, I'd suggest this approach instead...
```

## 🎯 Features

- **Natural conversation** - No commands, just chat!
- **Context memory** - They remember what you discussed
- **Personality** - Each expert has their own style
- **Switch experts** (unified chat) - Change mid-conversation
- **Web interface** - Clean, modern chat UI
- **Streaming responses** - See them type in real-time

## 📁 Files

- `quantum_chat.py` - Terminal chat with Alex
- `solver_chat.py` - Terminal chat with Sam
- `unified_expert_chat.py` - Terminal chat with both (type "switch to alex/sam")
- `expert_chat_app.py` - Web interface (Streamlit)
- `requirements.txt` - Python dependencies

## 🔑 Getting an API Key

1. Go to https://platform.openai.com
2. Sign up/login
3. Go to API keys section
4. Create new secret key
5. Copy and use it!

## 💡 Tips

- Ask for analogies when stuck
- Request code examples anytime
- Have them check your work
- Ask for practice problems
- Get their opinion on multiple approaches

Happy chatting! 🚀
