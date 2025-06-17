from flask import Flask

app = Flask(__name__)

@app.route('/user')
def hello_world():
    return "<p>Hello User Fix</p>"

@app.route('/edit')
def edit():
    return 'user edited'

@app.route('/delete')
def delete():
    return 'user deleted'

@app.route('dog')
def dog():
    return "dog created"