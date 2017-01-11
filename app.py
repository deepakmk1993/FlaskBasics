from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <head>
       <title>Flask Application</title>
    </head>
    <body>
        <h1>My First Flask Application</h1>
    </body>
    """
if __name__ == "__main__":
    app.run()