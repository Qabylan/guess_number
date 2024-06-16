from random import randint
from flask import Flask, render_template, request, session, redirect, url_for
import db

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    global question_num
    question_num = session['number'] = randint(1, 7)
    session['counter'] = 0
    message = 'Введите число от 1 до 7: (Вам даётся 3 попытки чтобы угадать)'
    db.insert_games()
    return render_template('index.html', message=message)

@app.route('/play', methods=['POST'])
def play():
    global answer_num
    answer_num = request.form['number_guess']
    db.insert_games_stat(question_num, answer_num)
    if 'counter' not in session:
        session['counter'] = 0

    if answer_num == '':
        message = 'Пожалуйста, введите число'
        return render_template('index.html', message=message)

    if int(answer_num) == question_num:
        message = "Поздравляю! Вы угадали число"
        return render_template('result.html', message=message)
    else:
        session['counter'] += 1
        if session['counter'] < 3:
            message = "Попробуйте ещё раз"
            return render_template('index.html', message=message)
        else:
            message = f"К сожалению попытки закончились, это было число {question_num}"
            return render_template('result.html', message=message)

@app.route('/noplay', methods=['POST'])
def noplay():
    message = 'Игра окончена'
    return render_template('result.html', message=message)

@app.route('/restart', methods=['POST'])
def restart():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)