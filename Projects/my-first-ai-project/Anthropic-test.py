import os
from anthropic import Anthropic

def anthropic_test():
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        messages = [
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        model = "claude-sonnet-4-6",
        max_tokens = 100
    )
    return response

def main():
    response = anthropic_test()
    print(response)

if __name__ == "__main__":
    main()