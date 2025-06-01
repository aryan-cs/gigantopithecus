import ollama

BACKUP_MODEL_NAME = "gemma3:1b"
MODEL_NAME = "jarvis"

def chat_with_model(model_name, conversation):
    reply = ''
    for chunk in ollama.chat(model=model_name, messages=conversation, stream=True):
        content = chunk['message']['content']
        print(content, end='', flush=True)
        reply += content
    return reply

def main():
    active_model = MODEL_NAME
    fallback_triggered = False

    conversation = []

    while True:
        user_input = input("\n> ")
        if user_input == "/bye":
            break

        conversation.append({'role': 'user', 'content': user_input})
        print('', end='', flush=True)

        try:
            reply = chat_with_model(active_model, conversation)
        except Exception as e:
            if not fallback_triggered:
                print(f"\n[Error with model '{MODEL_NAME}': {e}. Switching to backup model '{BACKUP_MODEL_NAME}']\n")
                fallback_triggered = True
                active_model = BACKUP_MODEL_NAME
                reply = chat_with_model(active_model, conversation)
            else:
                reply = chat_with_model(active_model, conversation)

        print()
        conversation.append({'role': 'assistant', 'content': reply})

if __name__ == "__main__":
    main()
