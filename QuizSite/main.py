from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = 0
    if request.method == "POST":
        questions = {
            "What does CPU stand for?": "central processing unit",
            "What does GPU stand for?": "graphics processing unit",
            "What does RAM stand for?": "random access memory",
            "What does PSU stand for?": "power supply unit"
        }
        for question, correct_answer in questions.items():
            user_answer = request.form.get(question).lower()
            if user_answer == correct_answer:
                score += 1
        return render_template("result.html", score=score)

    return render_template("quiz.html")

if __name__ == "__main__":
    app.run(debug=True)
