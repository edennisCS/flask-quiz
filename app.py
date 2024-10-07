from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load quiz questions from JSON file
def load_questions():
    with open('questions.json', 'r') as file:
        questions = json.load(file)
    return questions

@app.route('/')
def index():
    questions = load_questions()  # Load questions when rendering the index page
    return render_template('index.html', quiz_title="My Quiz", questions=questions)

@app.route('/result', methods=['POST'])
def result():
    questions = load_questions()  # Load questions to check answers
    score = 0
    for question in questions:
        user_answer = request.form.get(question["id"])
        if user_answer == question["answer"]:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
