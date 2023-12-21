from flask import Flask

app = Flask(__name__)

from web_flask import routes

app.url_map.strict_slashes = False

if __name__ == "__main__":
    """ app should be listening on 0.0.0.0 port 5000 """
    app.run(host="0.0.0.0", port=5000)