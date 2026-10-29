import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


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

