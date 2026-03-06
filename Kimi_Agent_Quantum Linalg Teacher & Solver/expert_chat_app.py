"""
Web-based Expert Chat App using Streamlit
Supports Ollama (Local), Grok (xAI), and OpenAI.
Run: streamlit run expert_chat_app.py
"""

import streamlit as st
import openai
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page config
st.set_page_config(
    page_title="Expert Chat - Linear Algebra & Problem Solving",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'messages_alex' not in st.session_state:
    st.session_state.messages_alex = [
        {"role": "system", "content": """You are Alex, a friendly expert in Linear Algebra for Quantum Computing.
        Talk conversationally like a knowledgeable friend. Use analogies, be encouraging, 
        and always connect concepts to quantum applications. Use Dirac notation when appropriate."""}
    ]
    st.session_state.messages_sam = [
        {"role": "system", "content": """You are Sam, a brilliant problem-solver friend.
        Talk like an expert buddy. Break down complex problems, give honest opinions,
        and suggest alternative approaches with trade-offs."""}
    ]

# Application hardcoded to use Grok (xAI) as the provider seamlessly
provider = "Grok (xAI)"
api_key = os.getenv("XAI_API_KEY", "")
ollama_model = "" # Defined to satisfy linter, but unused by Grok

if not api_key:
    st.sidebar.error("❌ XAI_API_KEY not found in .env file! Please add it to start.")

# Sidebar for expert selection
st.sidebar.title("🤖 Choose Your Expert")
expert_choice = st.sidebar.radio(
    "Who do you want to chat with?",
    ("🧮 Alex (Linear Algebra & Quantum)", "🔧 Sam (Problem Solver)")
)

# Set current expert
if "Alex" in expert_choice:
    current_expert = "alex"
    expert_name = "Alex"
    expert_emoji = "🧮"
    expert_desc = "Linear Algebra & Quantum Computing Expert"
    messages_key = "messages_alex"
else:
    current_expert = "sam"
    expert_name = "Sam"
    expert_emoji = "🔧"
    expert_desc = "Complex Problem Solver"
    messages_key = "messages_sam"

# Main interface
st.title(f"{expert_emoji} Chat with {expert_name}")
st.caption(expert_desc)

# Display chat messages
for msg in st.session_state[messages_key]:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

def generate_response(messages, provider, api_key):
    """Router to fetch responses from different providers"""
    if provider == "Ollama (Local & Free)":
        url = "http://localhost:11434/api/chat"
        payload = {
            "model": ollama_model,
            "messages": messages,
            "stream": True,
            "options": {
                "temperature": 0.7
            }
        }
        try:
            response = requests.post(url, json=payload, stream=True)
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        if "message" in data and "content" in data["message"]:
                            yield data["message"]["content"]
            else:
                yield f"❌ Request to Ollama failed: {response.text}"
        except requests.exceptions.ConnectionError:
            yield "❌ Could not connect to Ollama. Make sure Ollama is installed and running locally!"
            
    elif provider == "Grok (xAI)":
        if not api_key:
            yield "❌ Please provide a Grok (xAI) API Key in the .env file."
            return
        try:
            from openai import OpenAI
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.x.ai/v1"
            )
            print("Sending request to Grok API...")
            response = client.chat.completions.create(
                model="grok-3",
                messages=messages,
                temperature=0.7,
                stream=True
            )
            
            print("Grok connected, iterating chunks...")
            for chunk in response:
                if hasattr(chunk, 'choices') and chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            print(f"Grok explicit exception caught: {e}")
            yield f"❌ Grok API Error: {str(e)}"

    elif provider == "Groq (Fast & Free API)":
        if not api_key:
            yield "❌ Please provide a Groq API Key in the sidebar or .env file."
            return
        try:
            from openai import OpenAI
            # Using openai library to call Groq endpoint for simple compatibility
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.groq.com/openai/v1"
            )
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=messages,
                temperature=0.7,
                stream=True
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"❌ Groq API Error: {str(e)}"

    elif provider == "OpenAI":
        if not api_key:
            yield "❌ Please provide an OpenAI API Key in the sidebar or .env file."
            return
        try:
            from openai import OpenAI
            client = OpenAI(
                api_key=api_key
            )
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7,
                stream=True
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"❌ OpenAI API Error: {str(e)}"

# Chat input
if prompt := st.chat_input("What would you like to discuss?"):
    # Add user message
    st.session_state[messages_key].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner(f"{expert_name} is thinking..."):
            message_placeholder = st.empty()
            full_response = ""
            
            print(f"Requesting response from {provider}...")
            # Use generator to stream response
            try:
                for chunk in generate_response(st.session_state[messages_key], provider, api_key):
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")
            except Exception as outer_e:
                print(f"Outer exception caught: {outer_e}")
                full_response = f"❌ Error retrieving response: {str(outer_e)}"
            
            message_placeholder.markdown(full_response)
    
    # Save response
    if "❌" not in full_response and full_response.strip(): # Don't save empty/errors to chat history
        st.session_state[messages_key].append(
            {"role": "assistant", "content": full_response}
        )

# Clear chat button
if st.sidebar.button("Clear Chat"):
    if current_expert == "alex":
        st.session_state.messages_alex = [st.session_state.messages_alex[0]]
    else:
        st.session_state.messages_sam = [st.session_state.messages_sam[0]]
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown(f"""
### About {expert_name}

**{expert_desc}**

Ask anything! Some ideas:
- "Explain eigenvalues like I'm 5"
- "How do quantum gates work?"
- "Solve this optimization problem..."
- "What's the best algorithm for...?"
""")
