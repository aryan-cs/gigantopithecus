import ollama

# MODEL_NAME = "gemma3:1b"
MODEL_NAME = "king-louie"

def main():
    print(f"Now chatting with {MODEL_NAME}")
    conversation = []

    while True:
        user_input = input("> ")
        if user_input == "/bye":
            break

        conversation.append({'role': 'user', 'content': user_input})
        print('', end='', flush=True)

        reply = ''
        for chunk in ollama.chat(model=MODEL_NAME, messages=conversation, stream=True):
            content = chunk['message']['content']
            print(content, end='', flush=True)
            reply += content

        print()
        conversation.append({'role': 'assistant', 'content': reply})

if __name__ == "__main__":
    main()
