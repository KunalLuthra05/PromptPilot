from datetime import datetime


def log_request(prompt: str, model: str):
    print("\n" + "=" * 60)
    print("PromptPilot")
    print("=" * 60)
    print(f"Time           : {datetime.now().strftime('%H:%M:%S')}")
    print(f"Selected Model : {model}")
    print(f"Prompt         : {prompt}")
    print("=" * 60 + "\n")