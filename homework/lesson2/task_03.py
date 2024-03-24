# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age', type=int)
        try:
            age = int(age)
            if age < 18:
                return redirect(url_for('error'))
            else:
                return redirect(url_for('result', name=name, age=age))
        except ValueError:
            return redirect(url_for('error'))

    return render_template('task_03.html')


@app.route('/result/')
def result():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'<h1>Привет {name}! Ваш возраст {age} </h1>'


@app.route('/error/')
def error():
    return f'<h1>Ошибка, некорректный возраст!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
