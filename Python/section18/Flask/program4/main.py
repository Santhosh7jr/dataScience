from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def fn():
    return render_template("demo.html")

# @app.route("/submit", methods = ["POST"])
# def submit():
#     return f"Your name is: {request.form['nameSpace']}"

# Variable rule
@app.route("/success/<score>")
def success(score):
    return f"Your score is: {score}"

# variable rule
@app.route("/success2/<int:score>")
def success2(score):
    return f"Your score is: {str(score)}"

@app.route("/result/<int:score>")
def result(score):

    res = "PASSED" if (score > 50) else "FAILED"

    return render_template("result.html", results = res)

@app.route("/result2/<int:score>")
def result2(score):

    res = {
        "score" : str(score),
        "outcome" : "PASSED" if score > 50 else "FAILED"
    }

    return render_template("result2.html", results = res)

@app.route("/submit", methods=['POST'])
def submit():

    if request.form["nameSpace"] == "Santhosh":
        return redirect(url_for("result2", score = 100))
    else:
        return redirect(url_for("result2", score = 0))

if __name__ == "__main__":
    app.run()

