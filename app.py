from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "DevOps Pipeline Running 🚀"

@app.route('/cpu')
def cpu():
    import random
    return str(random.random())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)