from flask import Flask,render_template,session,redirect,request
from quiz import State,Trigger

app = Flask(__name__)
app.secret_key = "itsasecret"

RULES = {
    State.QUESTION_1 : [
        (Trigger.ANSWER_1, State.QUESTION_2),
        (Trigger.ANSWER_2, State.QUESTION_3),
    ],
    State.QUESTION_2 : [
        (Trigger.ANSWER_3, State.RESULT_1),
        (Trigger.ANSWER_4, State.QUESTION_3)
    ],
    State.QUESTION_3 : [
        (Trigger.ANSWER_5, State.RESULT_2),
        (Trigger.ANSWER_6, State.RESULT_1)
    ]
}

@app.route('/')
def index():
    if 'state' not in session:
        session['state'] = State.QUESTION_1
    return render_template('index.html',rules=RULES)

@app.post('/process_answer')
def process_answer():
    session['state'] = State(request.form['answer'])
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)