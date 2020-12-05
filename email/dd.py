from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def generate():
    return generate_password_hash('123456')


@app.route('/cheek/')
def cheek():
    if check_password_hash('pbkdf2:sha256:150000$7dXpkr3A$be18918aee29236282cf54ef7f82cbbb53a30f93329861f73da503c9a3994552', '123456'):
        return '1'
    return '0'


if __name__ == "__main__":
    app.run()
