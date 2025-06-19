import ollama
import pyttsx3
import re
import speech_recognition as sr

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
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    active_model = MODEL_NAME
    fallback_triggered = False
    conversation = []

    # Calibrate the recognizer for ambient noise
    with mic as source:
        print("Calibrating for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)
        print("Calibration complete.")

    while True:
        # Listen for user input via microphone
        print("\nListening...")
        try:
            with mic as source:
                audio = r.listen(source)
            
            user_input = r.recognize_google(audio)
            print(f"> {user_input}")

        except sr.UnknownValueError:
            print("Could not understand audio, please try again.")
            continue
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            continue

        if user_input.lower() == f"goodbye {MODEL_NAME}":
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
