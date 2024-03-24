# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        text = request.form.get('text')
        wrd_cnt = str(len(text))
        return f' Во введенном тексте {wrd_cnt} символ(a/ов)!'
    return render_template('task_01.html')


if __name__ == '__main__':
    app.run(debug=True)
