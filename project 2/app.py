from flask import Flask, render_template, request

app = Flask(__name__)

summaries = {
    "motivation": "Stay strong! You can achieve anything you focus on.",
    "study": "Study smart, take breaks, and keep learning every day.",
    "health": "Your health matters. Eat well, sleep well, move often.",
    "success": "Success comes to those who stay consistent."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summary", methods=["POST"])
def summary():
    topic = request.form.get("topic")
    result = summaries.get(topic, "No summary available.")
    return render_template("summary.html", topic=topic, result=result)

if __name__ == "__main__":
    app.run(debug=True,port=5001)
