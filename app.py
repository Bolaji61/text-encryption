from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/result', methods =['POST'])
def encrypt():
    text = request.form.get('fill')
    encrypt = Fernet(key)
    text = bytes(text, encoding = 'utf8')
    token = encrypt.encrypt(text)
    return render_template('result.html', token =token)

if __name__ == '__main__':
    app.run(debug = True, port='5000')
