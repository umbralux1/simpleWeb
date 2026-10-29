import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/', summary='Главная ручка', tags=['основные ручки'])
def home():
    return 'Hello World!fesfsesf!'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)


