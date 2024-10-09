from flask import Flask, render_template, render_template_string

app = Flask(__name__,
    template_folder='Front-End/dist',
    static_folder='Front-End/dist/assets')

@app.route("/")
def index():
    return render_template('index.html')
