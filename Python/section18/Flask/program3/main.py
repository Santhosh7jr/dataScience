from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def fn():
    return render_template("index.html")

@app.route("/form", methods=['GET', 'POST'])
def fn2():
    if request.method == 'POST':
        return f"<h1>Your Nmae is: {request.form["nameSpace"]}</h1>"
    return render_template("form.html")

if __name__ == "__main__":
    app.run()