from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {'title': 'Главная'}
    return render_template('base_01.html')


@app.route('/clothing/')
def clothing():
    context = {'title': 'Одежда'}
    return render_template('clothing.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def jacket():
    context = {'title': 'Куртка'}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run()
