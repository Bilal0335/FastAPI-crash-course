from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
# Book data model - id, title, author aur genre fields hain

class Book(BaseModel):
    id:int
    title:str
    author:str


# In-memory list jisme books store hongi
books : List[Book] = []

@app.get("/")
def home():
    return {"message": "Welcome to the Book API! Use /books endpoint to manage books."}

@app.get("/books")
def get_all_books():
    return books

@app.post("/books")
def add_book(book:Book):
    books.append(book)
    return {"message": "Book added successfully!", "book": book}

@app.put("/books/{book_id}")
def update_bbok(book_id:int,update_book:Book):
    for index,book in enumerate(books):
        if book.id == book_id:
            books[index] = update_book
            return {"message": "Book updated successfully!", "book": update_book}
    return {"error": "Book not found!"}

@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for index, book in enumerate(books):
        if book.id == book_id:
            remove_book = books.pop(index)
            return {"message": "Book deleted successfully!", "book": remove_book}
    return {"error": "Book not found!"}
