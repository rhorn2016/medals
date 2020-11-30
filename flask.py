from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from CollabTech'

app.run(debug=True, port=8080, host='0.0.0.0')