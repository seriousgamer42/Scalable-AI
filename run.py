from core.engine import AICore
from config.config_loader import load_config

def main():
    config = load_config()
    ai = AICore(config)

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit", "shutdown"]:
            break

        response = ai.process_input(user_input)
        print("AI:", response)

        # Optional: Reflect after each step
        ai.reflect_and_adapt()

if __name__ == "__main__":
    main()