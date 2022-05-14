import flask
import numbers
import importlib.util

def _try():
    return 0

app = flask.Flask(__name__)

#@app.route(_try, methods=["GET"]) set a route to send data 


if __name__ == "__main__":
    app.run