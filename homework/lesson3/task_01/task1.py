# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.


from flask import Flask, render_template
from models_01 import db, Author, Book
from random import choice, randint, random, Random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Books_Authors.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-user")
def add_author():
    for _ in range(1, 11):
        author = Author(name=choice(['Alex', 'Kim', 'Petrushka']), surname=choice(['One', 'Two', 'Three']))
        db.session.add(author)
    db.session.commit()

    for i in range(1, 11):
        book = Book(name=f'name{i}', year=randint(1917, 2012), count=randint(1, 5), author_id=randint(1, 10))
        db.session.add(book)
    db.session.commit()


@app.route('/')
def index():
    book = db.session.query(Book)
    return render_template('index.html', book=book)


if __name__ == '__main__':
    app.run(debug=True)
