#!/usr/bin/env python3
"""
Setup script for FREE LLM options
Run: python setup_free.py
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and show output"""
    print(f"\n📦 {description}...")
    print(f"   Command: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"   ✅ Success")
        return True
    else:
        print(f"   ❌ Failed: {result.stderr}")
        return False

def check_python():
    """Check Python version"""
    print("="*60)
    print("🔍 CHECKING PYTHON")
    print("="*60)
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    if version < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    print("✅ Python version OK")
    return True

def setup_groq():
    """Setup Groq option"""
    print("\n" + "="*60)
    print("🔧 SETTING UP GROQ (Recommended)")
    print("="*60)
    
    # Install groq package
    run_command("pip install groq", "Installing groq package")
    
    # Check for API key
    key = os.getenv("GROQ_API_KEY")
    if key:
        print("✅ GROQ_API_KEY is set")
    else:
        print("\n⚠️  GROQ_API_KEY not set")
        print("\nTo get your FREE API key:")
        print("1. Go to: https://console.groq.com")
        print("2. Sign up (free, no credit card)")
        print("3. Create an API key")
        print("4. Set it: export GROQ_API_KEY='your-key'")
        
        key_input = input("\nPaste your Groq API key (or press Enter to skip): ").strip()
        if key_input:
            # Save to .env file
            with open(".env", "a") as f:
                f.write(f"\nGROQ_API_KEY={key_input}\n")
            print("✅ Saved to .env file")
            os.environ["GROQ_API_KEY"] = key_input
    
    return True

def setup_ollama():
    """Setup Ollama option"""
    print("\n" + "="*60)
    print("🔧 SETTING UP OLLAMA (Local)")
    print("="*60)
    
    # Check if Ollama is installed
    result = subprocess.run("which ollama", shell=True, capture_output=True)
    if result.returncode == 0:
        print("✅ Ollama is installed")
        
        # Check if running
        try:
            import requests
            response = requests.get("http://localhost:11434/api/tags", timeout=3)
            if response.status_code == 200:
                print("✅ Ollama is running")
                models = response.json().get("models", [])
                if models:
                    print(f"✅ Models available: {len(models)}")
                else:
                    print("⚠️  No models downloaded")
                    print("\nDownload a model:")
                    print("  ollama pull llama3.1:8b  (8GB RAM)")
                    print("  ollama pull mistral-nemo  (12GB RAM)")
                    print("  ollama pull llama3.1:70b  (48GB RAM)")
            else:
                print("⚠️  Ollama not running")
                print("   Start it: ollama serve")
        except:
            print("⚠️  Ollama not running")
            print("   Start it: ollama serve")
    else:
        print("⚠️  Ollama not installed")
        print("\nTo install Ollama:")
        print("  macOS/Linux: curl -fsSL https://ollama.com/install.sh | sh")
        print("  Windows: Download from https://ollama.com")
        print("\nThen download a model:")
        print("  ollama pull llama3.1:8b")
    
    return True

def create_env_file():
    """Create .env file if not exists"""
    if not os.path.exists(".env"):
        print("\n📝 Creating .env file...")
        with open(".env", "w") as f:
            f.write("# Add your API keys here\n")
            f.write("# GROQ_API_KEY=your_key_here\n")
            f.write("# OPENAI_API_KEY=your_key_here\n")
        print("✅ Created .env file")

def main():
    print("="*60)
    print("🤖 FREE LLM SETUP")
    print("="*60)
    print("\nThis will set up FREE options for your expert chat!")
    print("No paid APIs required! 🎉\n")
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Setup options
    print("\n" + "="*60)
    print("📋 SETUP OPTIONS")
    print("="*60)
    print("\n1. Groq API (Recommended)")
    print("   - Easiest setup")
    print("   - 1.5M free tokens/day")
    print("   - Best quality models")
    print("   - Requires internet")
    print("\n2. Ollama (Local)")
    print("   - 100% free forever")
    print("   - 100% private")
    print("   - Works offline")
    print("   - Requires good hardware")
    print("\n3. Both (Recommended for flexibility)")
    print("   - Use Groq for speed")
    print("   - Use Ollama for privacy")
    
    choice = input("\nWhich option? (1/2/3): ").strip()
    
    if choice == "1":
        setup_groq()
    elif choice == "2":
        setup_ollama()
    elif choice == "3":
        setup_groq()
        setup_ollama()
    else:
        print("Invalid choice. Setting up both...")
        setup_groq()
        setup_ollama()
    
    # Summary
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    print("\nYou can now run:")
    print("  python expert_chat_universal.py  # Auto-detects best option")
    print("  python expert_chat_groq.py       # Groq specifically")
    print("  python expert_chat_ollama.py     # Ollama specifically")
    print("\nFor more info, see: FREE_OPTIONS_GUIDE.md")
    print("="*60)

if __name__ == "__main__":
    main()
