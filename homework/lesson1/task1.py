from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def base():
    context = {'title': 'Главная'}
    return render_template('base.html', **context)


@app.route('/about/')
def about():
    context = {'title': 'О нас'}
    return render_template('about.html', **context)


@app.route('/contacts/')
def concats():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run()
