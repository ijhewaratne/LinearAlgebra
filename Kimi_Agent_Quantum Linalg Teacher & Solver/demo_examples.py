"""
Demo: Example conversations with your experts
Run: python demo_examples.py
"""

examples = {
    "alex": [
        {
            "user": "Hey Alex! I'm new to quantum computing. Where should I start with linear algebra?",
            "context": "First conversation, beginner level"
        },
        {
            "user": "Can you explain what a qubit really is using vectors?",
            "context": "Connecting abstract math to physical meaning"
        },
        {
            "user": "Show me how to calculate the probability of measuring |0⟩ in this state: |ψ⟩ = (1/√2)|0⟩ + (1/√2)|1⟩",
            "context": "Practical calculation with Dirac notation"
        },
        {
            "user": "Why do we need tensor products for multiple qubits?",
            "context": "Understanding multi-qubit systems"
        },
        {
            "user": "Walk me through finding the eigenvalues of the Pauli-X matrix",
            "context": "Step-by-step problem solving"
        }
    ],
    "sam": [
        {
            "user": "Sam, I have this optimization problem: minimize f(x) = x² + 4x + 5. What's the best approach?",
            "context": "Mathematical optimization"
        },
        {
            "user": "I'm trying to solve a system of 100 linear equations. Should I use Gaussian elimination or matrix inversion?",
            "context": "Algorithm selection with trade-offs"
        },
        {
            "user": "Here's my quantum circuit design [describes circuit]. Can you check if this will create entanglement?",
            "context": "Quantum computing problem with opinion"
        },
        {
            "user": "What's the time complexity of Shor's algorithm, and is there any practical limitation I'm missing?",
            "context": "Complexity analysis with practical considerations"
        },
        {
            "user": "I need to diagonalize this 3x3 matrix for my physics problem. Can you solve it and tell me if there's a faster way?",
            "context": "Linear algebra problem with alternative approaches"
        }
    ]
}

print("="*60)
print("🤖 EXAMPLE CONVERSATIONS WITH YOUR EXPERTS")
print("="*60)

print("\n" + "🧮 ALEX (Linear Algebra & Quantum Expert)".center(60))
print("-"*60)
for i, ex in enumerate(examples["alex"], 1):
    print(f"\n{i}. You: \"{ex['user']}\"")
    print(f"   Context: {ex['context']}")

print("\n" + "🔧 SAM (Problem Solver)".center(60))
print("-"*60)
for i, ex in enumerate(examples["sam"], 1):
    print(f"\n{i}. You: \"{ex['user']}\"")
    print(f"   Context: {ex['context']}")

print("\n" + "="*60)
print("💡 TIPS FOR GREAT CONVERSATIONS")
print("="*60)
tips = [
    "Start with 'Hey [name]!' to set a friendly tone",
    "Ask for analogies: 'Explain this like I'm 5'",
    "Request step-by-step: 'Walk me through this slowly'",
    "Ask for opinions: 'Is this the best approach?'",
    "Get code: 'Can you show me Python code for this?'",
    "Check understanding: 'Can you give me a practice problem?'",
    "Go deep: 'Why does this work mathematically?'",
    "Connect concepts: 'How does this relate to [topic]?'"
]
for tip in tips:
    print(f"  • {tip}")

print("\n" + "="*60)
print("Ready to chat? Run one of the chat scripts!")
print("="*60)
