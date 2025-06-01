
# Gigantopithecus

An all-in-one personal assistant w/ integrations like Google Calendar, Email, and Internet access running on a fine-tuned, lightweight LLM. 

## Installation & Setup

To interact with the model, follow these steps:

1. Download [Ollama](https://ollama.com/download)
2. Setup your virtual environment
```
python -m venv genv

```
3. Create King Louie from the model file
```
ollama create king-louie -f Modelfile
```
4. Activate the virtual environment  
Windows: `genv\Scripts\activate`  
macOS/Linux: `source genv/bin/activate`  

5. Run the program
```
python main.py
```

### Notes

- You may need to copy your local ollama installation into your virtual environment!

## To-Do

- [x] Setup basic chatbot interation
- [x] Enable model customization
- [ ] Incorporate RAG
- [ ] Enable Internet access + search functionality
- [ ] Develop support for G Suite

##

![Gigantopithecus](https://raw.githubusercontent.com/aryan-cs/gigantopithecus/refs/heads/master/gigantopithecus.jpg)
