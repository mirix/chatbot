from flask import Flask, render_template, request
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

name = 'bigscience/T0_3B'
device = "cpu"
print(f"Device: {device}")

print("Start loading model...")

tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForSeq2SeqLM.from_pretrained(name, device_map='auto')

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    try: chat_history
    except NameError: chat_history = ''
    user_input = request.args.get('msg')
    bot_input_ids = tokenizer(chat_history + user_input + tokenizer.eos_token, return_tensors='pt').input_ids.to(device)
    chat_history_ids = model.generate(bot_input_ids, max_length=1024, pad_token_id=tokenizer.eos_token_id)
    chat_history = tokenizer.decode(chat_history_ids[0])
    return chat_history

if __name__ == "__main__":
    app.run(host='0.0.0.0') 
