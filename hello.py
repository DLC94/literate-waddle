from flask import Flask

app = Flask(__name__)

@app.route('/user')
def hello_world():
    return "<p>Hello !User</p>"

@app.route('/edit')
def edit():
    return 'user edited'

@app.route('/delete')
def delete():
    return 'user deleted'

@app.route('/app')
def app():
    return 'app created'