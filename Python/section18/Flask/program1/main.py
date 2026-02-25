from flask import Flask

app = Flask(__name__)

@app.route("/")
def fn():
    return "<h1>Welcome to the flask app</h1>"

if __name__ == "__main__":
    app.run()