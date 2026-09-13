from core.engine import AICore
from config.config_loader import load_config


def main():
    config = load_config()
    ai = AICore(config)

    print("Scalable AI online. Type 'exit' to shut down.")

    while True:
        try:
            user_input = input(">> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down.")
            break

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "shutdown"]:
            print("Shutting down.")
            break

        try:
            response = ai.process_input(user_input)
            print("AI:", response)

            # Optional self-reflection/adaptation step.
            ai.reflect_and_adapt()
        except Exception as exc:
            print(f"AI error: {exc}")


if __name__ == "__main__":
    main()
