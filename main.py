from flask import Flask, render_template
import threading
import json
from duolingo_request import run_make_request

app = Flask(__name__)

@app.route('/')
def home():
    with open("response_output.json", 'r') as json_file:
        response_data = json.load(json_file)
    return render_template('index.html', response_data=response_data)

if __name__ == '__main__':
    threading.Thread(target=run_make_request, daemon=True).start()
    app.run(host='0.0.0.0', port=3000)
