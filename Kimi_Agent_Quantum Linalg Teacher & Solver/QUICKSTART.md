# 🚀 Quick Start Guide

Get your expert chat running in **2 minutes** for FREE!

---

## ⚡ Fastest Path (Recommended)

### Step 1: Get Free API Key (1 minute)
```bash
# Go to https://console.groq.com
# Sign up (free, instant)
# Create API key
# Copy the key
```

### Step 2: Set Key & Run (1 minute)
```bash
# In terminal:
export GROQ_API_KEY="gsk_your_key_here"

# Install package
pip install groq

# Run chat
python expert_chat_groq.py
```

### Step 3: Chat!
```
🧮 Alex: Hey! I'm Alex, your linear algebra buddy for quantum! 
         What should we explore?

You: Hey Alex! Can you explain what a tensor product is?

Alex: Hey! Great question! Think of it like building with LEGO blocks...
```

---

## 🎯 What You Get

Two expert friends:
- **🧮 Alex** - Linear Algebra & Quantum Computing expert
- **🔧 Sam** - Complex Problem Solver

Switch anytime by typing: `switch to alex` or `switch to sam`

---

## 📂 All Files Explained

| File | Purpose | When to Use |
|------|---------|-------------|
| `expert_chat_groq.py` | Uses Groq API (free tier) | **Easiest, recommended** |
| `expert_chat_ollama.py` | Runs models locally | For privacy, offline use |
| `expert_chat_universal.py` | Auto-detects best option | Flexible, tries all |
| `setup_free.py` | Setup helper | First time setup |
| `FREE_OPTIONS_GUIDE.md` | Detailed comparison | Choosing best option |
| `QUICKSTART.md` | This file | Getting started fast |

---

## 🔄 Switching Between Free Options

### Option A: Groq (Cloud API)
- ✅ Easiest setup
- ✅ Best quality (Llama 3 70B)
- ✅ 1.5M free tokens/day
- ❌ Requires internet

```bash
export GROQ_API_KEY="your-key"
pip install groq
python expert_chat_groq.py
```

### Option B: Ollama (Local)
- ✅ 100% free forever
- ✅ 100% private
- ✅ Works offline
- ❌ Needs good hardware

```bash
# Install Ollama from https://ollama.com
ollama pull llama3.1:8b
python expert_chat_ollama.py
```

### Option C: Universal (Auto-Detect)
- ✅ Tries Groq first, falls back to Ollama
- ✅ Best of both worlds

```bash
# Set up both (see above)
python expert_chat_universal.py
```

---

## 💬 Example Conversations

### With Alex (Linear Algebra)
```
You: Hey Alex! What's a Hermitian operator and why do we care?

Alex: Hey! So a Hermitian operator is basically the quantum version 
of a real number. In math terms, it's an operator that's equal to 
its own conjugate transpose: H = H†

Here's why we care in quantum:
1. They have REAL eigenvalues → measurement outcomes are real
2. Their eigenvectors are orthogonal → distinct states
3. They represent physical observables (energy, spin, etc.)

Think of it like this: when you measure something in quantum 
mechanics, you need to get a real number, right? Hermitian 
operators guarantee that!

Want me to show you how to check if a matrix is Hermitian?
```

### With Sam (Problem Solver)
```
You: Sam, I need to solve this system: 2x + 3y = 7, x - y = 1

Sam: Ooh, let's crack this! *cracks knuckles*

So we have:
  2x + 3y = 7
   x -  y = 1

Method 1: Substitution (my go-to for small systems)
From eq2: x = y + 1
Substitute into eq1: 2(y+1) + 3y = 7
                     2y + 2 + 3y = 7
                     5y = 5
                     y = 1
Then x = 1 + 1 = 2

Solution: x=2, y=1 ✓

But here's my opinion: for 2x2, substitution is fine. But if you 
had 10 equations, I'd say use matrix methods (Gaussian elimination 
or numpy.linalg.solve). Want me to show you the matrix approach 
just for fun?
```

---

## 🛠️ Troubleshooting

### "No module named 'groq'"
```bash
pip install groq
```

### "GROQ_API_KEY not set"
```bash
export GROQ_API_KEY="your-key-here"
# Or add to ~/.bashrc or ~/.zshrc
```

### "Ollama connection refused"
```bash
# Make sure Ollama is running
ollama serve

# In another terminal:
python expert_chat_ollama.py
```

### "Out of memory" (Ollama)
```bash
# Use smaller model
ollama pull llama3.1:8b  # Instead of 70b
```

---

## 🎓 Tips for Great Conversations

1. **Be casual** - "Hey Alex!" or "Sam, quick question..."
2. **Ask for analogies** - "Explain like I'm 5"
3. **Get code** - "Show me Python for this"
4. **Ask opinions** - "Is this the best way?"
5. **Go deep** - "Why does this work?"
6. **Practice** - "Give me a problem to solve"

---

## 🚀 Next Steps

1. **Start chatting** with Alex or Sam
2. **Try both** experts - they have different strengths
3. **Switch backends** - Try Groq for speed, Ollama for privacy
4. **Customize** - Edit the prompts to change their personalities

---

## 📚 Learn More

- `FREE_OPTIONS_GUIDE.md` - Complete comparison of all free options
- `README.md` - Original documentation
- Online: https://console.groq.com - Get your free API key

---

**Ready? Get your Groq key and start chatting!** 🎉
