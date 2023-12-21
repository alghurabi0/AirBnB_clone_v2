from web_flask import app

@app.route("/")
def hello_HBNB():
    return"<p>Hello HBNB!</p>"