import ollama
import pyttsx3
import re

BACKUP_MODEL_NAME = "gemma3:1b"
MODEL_NAME = "jarvis"

def stream_and_speak(model_name, conversation, engine):
    sentence_buffer = ""
    full_reply = ""
    
    stream = ollama.chat(model=model_name, messages=conversation, stream=True)

    for chunk in stream:
        content = chunk['message']['content']
        print(content, end='', flush=True)
        full_reply += content
        sentence_buffer += content

        while True:
            match = re.search(r'[.?!]\s', sentence_buffer)
            
            if match:
                end_index = match.start() + 1
                to_speak = sentence_buffer[:end_index]
                
                engine.say(to_speak.strip())
                engine.runAndWait()
                
                sentence_buffer = sentence_buffer[match.end():]
            else:
                break

    if sentence_buffer.strip():
        engine.say(sentence_buffer.strip())
        engine.runAndWait()
    
    print()
    return full_reply

def main():
    engine = pyttsx3.init()
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
            reply = stream_and_speak(active_model, conversation, engine)
        except Exception as e:
            if not fallback_triggered:
                print(f"\n[Error with model '{MODEL_NAME}': {e}. Switching to backup model '{BACKUP_MODEL_NAME}']\n")
                fallback_triggered = True
                active_model = BACKUP_MODEL_NAME
                reply = stream_and_speak(active_model, conversation, engine)
            else:
                reply = stream_and_speak(active_model, conversation, engine)

        conversation.append({'role': 'assistant', 'content': reply})

if __name__ == "__main__":
    main()
