from flask import Flask, render_template, render_template_string, send_from_directory

app = Flask(__name__, static_folder='Front-End/dist', static_url_path='')

@app.route("/")
def index():
    return send_from_directory('Front-End/dist', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)