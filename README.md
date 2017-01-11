# Deploy Flask Application to Heroku
    pip install virtualenv virtualenvwrapper
    mkvirtualenv flask
    pip install flask gunicorn
    pip freeze > requirements.txt

--------------------------------
[How to install Flask on Cloud9?](https://c9.io/santiagobasulto_1/flask-example)
--------------------------------
To install the Flask package the easy_install python module should be used:
    
    $ sudo easy_install Flask
    $ pip install virtualenv virtualenvwrapper
    $ mkvirtualenv flask-example
    $ pip install Flask

--------------------------------
Running your flask App
--------------------------------
Cloud9 allows you to write webapps and expose them to the world.
You only have to be sure to bind your server to $IP:$PORT and you can access with the following scheme: https://projectname-c9-username.c9.io/
In flask it's as easy as:

    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host=host, port=port)

--------------------------------
Another Method
--------------------------------
In app.py

    import os
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'Hello World'
    
    app.run(debug=False, host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

--------------------------------
To Run the Application
--------------------------------
$ python app.py
