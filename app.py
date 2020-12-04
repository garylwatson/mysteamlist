from flask import Flask, render_template, request
from userProfile import loginFcn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    user = request.form['user']
    id = request.form['pass']
    result = loginFcn(user, id)
    if result == "Welcome back!":
        return render_template('profile.html')
    elif result == "Bulit":
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)