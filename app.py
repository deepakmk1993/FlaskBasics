import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <head>
       <title>Flask Application</title>
    </head>
    <body>
        <h1>My First Flask Application</h1>
    </body>
    """
@app.route('/<name>')
def index(name='Treehouse'):
    return render_template("index.html", name=name)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template("add.html", **context)

if __name__ == "__main__":
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host=host, port=port)