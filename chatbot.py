def run_chatbot():
    # Knowledge Base: Dictionary mapping user intents to responses ($O(1)$ lookup)
    responses = {
        "hello": "Hi there! Welcome to DecodeLabs. How can I assist you today?",
        "hi": "Hello! Ready to build some logic engines?",
        "project": "Project 1 requires a rule-based chatbot using dictionaries and a continuous loop.",
        "internship": "You are currently in your foundation phase training as an AI Engineer.",
        "i need internship details": "You are in Batch 2026, working on foundational rule-based AI systems.",
        "how i build my skills": "By practicing hands-on coding, writing clean logic, and experimenting with unique features!",
        "help": "I can respond to greetings, project info, and internship details. Type 'exit' to quit.",
        "bye": "Goodbye! Have a great day ahead."
    }

    print("--- DecodeLabs AI Guardrail System Online ---")
    print("Type 'exit' at any time to terminate the session.\n")

    # The Heartbeat: Infinite Loop
    while True:
        # Phase 1: Input & Sanitization (Normalization)
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()

        # Exit Strategy: Kill Command
        if clean_input == "exit":
            print("Bot: Shutting down logic engine. Goodbye!")
            break

        # Process & Response Engine: Atomic operation using .get() with fallback
        reply = responses.get(clean_input, "I do not understand that command. Type 'help' for options.")
        
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    run_chatbot()