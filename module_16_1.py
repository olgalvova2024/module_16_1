import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def home_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_page_info(username: str, age: int) -> dict:
    return {"Информация о пользователе. Имя": username, "Возраст": age}

if __name__ == '__main__':
    uvicorn.run('module_16_1:app')
