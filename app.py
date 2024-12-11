from flask import Flask, render_template
import os

app = Flask(__name__)
app.template_folder = 'templates'

@app.route("/")
def index():
    try:
        with open('/data/message.txt', 'r') as f:
            message = f.read()
    except FileNotFoundError:
        message = "Файл с текстом не найден."
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)