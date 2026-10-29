import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, ConfigDict


app = FastAPI()

data_without_age = {
    'email': 'sefsfesfsefsef@mail.ru',
    'bio': 'bla bla'
}

data = {
    'email': 'sfese@mail.ru',
    'age': 30,
    'bio': 'sefefsees',
    # 'birthday': '1990-01-01',
    # 'gender': 'male',
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')


users = []


@app.post('/users', tags=['Пользователи 💁‍'], summary='Добавить нового пользователя')
def add_user(user: UserSchema):
    users.append(user)
    return {'success': True, 'message': 'Пользователь успешно добавлен'}


@app.get('/users', tags=['Пользователи 💁‍'], summary='Получить всех пользователей')
def get_user() -> list[UserSchema]:
    return users


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)


print(repr(UserSchema(**data_without_age)))
print(repr(UserAgeSchema(**data)))


@app.get('/', summary='Главная ручка', tags=['основные ручки'])
def home():
    return 'Hello World!'


class NewBook(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
]


@app.get('/books', summary='Получить все книги', tags=['Книги 📚'])
def read_books():
    return books


@app.get('/books/{book_id}', summary='Получить конкретную книгу', tags=['Книги 📚'])
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail='Книга не найдена')


@app.post('/books', tags=['Книги 📚'], summary='Добавить новую книгу')
def create_book(new_book: NewBook):
    books.append({
        'title': new_book.title,
        'author': new_book.author,
        'id': len(books) + 1
    })
    return {'success': True, 'message': 'Книга успешно добавлена'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

