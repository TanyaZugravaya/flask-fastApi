# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.
# Реализуйте валидацию данных запроса и ответа
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [
    User(id=1, name="Alice", email="alice@mail.com", password="password1"),
    User(id=2, name="Bob", email="bob@mail.com", password="password2"),
]


@app.get("/users/", response_class=HTMLResponse)
async def get_user(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, "users": users})


@app.post("/users/", response_model=User)
async def create_user(u: User):
    users.append(u)
    return u


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    for index, u in enumerate(users):
        if u.id == user_id:
            users[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, u in enumerate(users):
        if u.id == user_id:
            del users[index]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("task_01:app", host="127.0.0.1", port=8000)
