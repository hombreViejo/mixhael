import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
print(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def hello_world():
    return 'Jellow, Jellow, World!'

@app.route('/main')
def main_page():
    return render_template('index.html')
