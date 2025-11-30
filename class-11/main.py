# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/Testing")
# async def root():
#     return {"message": "Hello World",
#             "status": 200,
#             "version": "1.0.0",
#             "env": "development"
#             }

# @app.get("/production")
# async def production():
#     return  {
#                 "message": "Hello World",
#                 "status": 200,
#                 "version": "1.0.0",
#                 "env": "production"
#             }
# @app.get("/staging")
# async def staging():
#     return  {
#                 "message": "Hello World",
#                 "status": 200,
#                 "version": "1.0.0",
#                 "env": "staging"
#             }
    
# @app.post("/post")
# async def post():
#     return  {
#                 "message": "Hello World",
#                 "status": 200,
#                 "version": "1.0.0",
#                 "env": "staging"
#             }
    
# @app.put("/put")
# async def put():
#     return  {
#                 "message": "Hello World PUt",
#                 "status": 200,
#                 "version": "1.0.0",
#                 "env": "staging"
#             }
# @app.delete("/delete")
# async def delete():
#     return  {
#                 "message": "Hello World",
#                 "status": 200,
#                 "version": "1.0.0",
#                 "env": "staging"
#             }
    

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI()

class Book(BaseModel):
    id : int
    title :str
    author : str
    price : float
    
Books : List[Book] = []

@app.get("/books", response_model=List[Book])
async def get_books():
    return "Welcome to the book store"

@app.post("/books", response_model=Book)
async def add_books(Book : Book):
    app.append(Book)
    return Book

@app.put("/Books/{book_id:id}", response_model=Book)
def Update_Book(book_id :int, Updated_Book : Book):
#    for index, book in enumerate(Books):
    for index, book in enumerate(Books):
        if book.id == book_id:
            Books[index] = Updated_Book
            # books[index] = Updated_Book
            return Updated_Book

raise HTTPException(status_code=404, detail="Book not found")  
            
@app.delete("/books/{book_id:id}")
async def delete_book(book_id : int):
    for index, book in enumerate(Books):
        if book.id == book_id:
            Books.pop(index)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)