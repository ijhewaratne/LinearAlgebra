#!/usr/bin/env python3
"""
Setup script for Expert Chat
Run: python setup.py
"""

import os
import sys

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    os.system(f"{sys.executable} -m pip install -r requirements.txt")
    print("✅ Dependencies installed")

def setup_api_key():
    """Guide user to set up API key"""
    print("\n" + "="*60)
    print("🔑 API KEY SETUP")
    print("="*60)
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        print("✅ OPENAI_API_KEY is already set!")
        return
    
    print("\nTo use the expert chat, you need an OpenAI API key.")
    print("\n1. Go to: https://platform.openai.com")
    print("2. Sign up or log in")
    print("3. Navigate to API keys section")
    print("4. Create a new secret key")
    print("5. Copy the key")
    
    print("\nThen choose how to set it:")
    print("\nOption A - Environment variable (recommended):")
    print("  export OPENAI_API_KEY='your-key-here'")
    
    print("\nOption B - .env file:")
    print("  cp .env.example .env")
    print("  # Edit .env and add your key")
    
    key = input("\nPaste your API key here (or press Enter to skip): ").strip()
    
    if key:
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={key}\n")
        print("✅ API key saved to .env file")
    else:
        print("⚠️  You'll need to set the API key before running the chat")

def main():
    print("="*60)
    print("🤖 EXPERT CHAT SETUP")
    print("="*60)
    
    check_python_version()
    install_requirements()
    setup_api_key()
    
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    print("\nYou can now run:")
    print("  python quantum_chat.py      # Chat with Alex (Linear Algebra)")
    print("  python solver_chat.py       # Chat with Sam (Problem Solver)")
    print("  python unified_expert_chat.py  # Chat with both!")
    print("  streamlit run expert_chat_app.py  # Web interface")
    print("\n  python demo_examples.py     # See example conversations")
    print("="*60)

if __name__ == "__main__":
    main()
