# Gigantopithecus

An all-in-one personal assistant w/ integrations like Google Calendar, Email, and Internet access running on a fine-tuned, lightweight LLM. 

## Installation & Setup

To interact with the model, follow these steps:

1. Download [Ollama](https://ollama.com/download)
2. Setup your virtual environment & libraries  
   **Windows**: 
   ```
   python -m venv genv
   genv\Scripts\activate
   pip install requirements.txt
   ```
   **macOS/Linux**:
   ```
    python3 -m venv genv
    source genv/bin/activate
    pip install -r requirements.txt
    ```
3. Create agent from the model file:
    ```
    ollama create king-louie -f modelfiles/KingLouie/ModelFile
    ```
4. Run the program:
    ```
    python main.py
    ```

### Notes

- You may need to copy your local ollama installation into your virtual environment!

### Currently Available Models
- **King Louie** [`king-louie`]: The default model, a friendly and helpful assistant.
- **Jarvis** [`jarvis`]: Inspired by Tony Stark's personal assistant.

## To-Do

- [x] Setup basic chatbot interation
- [x] Enable model customization
- [x] Implement text-to-speech functionality
- [x] Implement speech-to-text functionality
- [ ] Incorporate RAG
- [ ] Add support for Google Calendar
- [ ] Add support for Email
- [ ] Enable Internet access + search functionality

##

![Gigantopithecus](https://raw.githubusercontent.com/aryan-cs/gigantopithecus/refs/heads/master/gigantopithecus.jpg)
