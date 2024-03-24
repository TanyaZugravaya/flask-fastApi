# Создайте форму регистрации пользователей в приложении Flask. Форма должна
# содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
# формы данные должны валидироваться на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class RegistrationForm(FlaskForm):
    first_name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(), Length(min=8),  validators.Regexp(r'[A-Za-z0-9]+', message='Пароль должен содержать хотя бы одну букву и одну цифру')])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[validators.DataRequired(), EqualTo('password', message='Пароли не совпадают ')])


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == ['POST'] and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        print(first_name, last_name, email, password, confirm_password)

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
