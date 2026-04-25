"""
Run with:
    pip install fastapi uvicorn
    uvicorn main:app --reload

Interactive docs available at:
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional
import json
# import os
from pathlib import Path

# ── App setup ──────────────────────────────────────────────────────────────
app = FastAPI(
    title="📚 Books API",
    description="Educational FastAPI demo — shows GET, POST, PUT, PATCH, DELETE",
    version="1.0.0",
)

CWD = Path.cwd()
DATA_FILE = CWD / "books.json"


# ── Helpers ─────────────────────────────────────────────────────────────────
def load_books() -> dict:
    """Read books from JSON file. Return empty dict if file doesn't exist."""
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_books(books: dict) -> None:
    """Persist books dict to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=2)


def next_id(books: dict) -> int:
    """Generate the next integer ID."""
    return max((int(k) for k in books), default=0) + 1


# ── Schemas ─────────────────────────────────────────────────────────────────
class BookCreate(BaseModel):
    """Fields required when creating a new book."""
    title: str = Field(..., example="The Pragmatic Programmer")
    author: str = Field(..., example="David Thomas")
    year: int = Field(..., ge=1000, le=2100, example=1999)
    genre: Optional[str] = Field(None, example="Technology")


class BookUpdate(BaseModel):
    """All fields required — used for full replacement (PUT)."""
    title: str = Field(..., example="The Pragmatic Programmer")
    author: str = Field(..., example="Andrew Hunt")
    year: int = Field(..., ge=1000, le=2100, example=1999)
    genre: Optional[str] = Field(None, example="Technology")


class BookPatch(BaseModel):
    """All fields optional — used for partial update (PATCH)."""
    title: Optional[str] = Field(None, example="Clean Code")
    author: Optional[str] = Field(None, example="Robert C. Martin")
    year: Optional[int] = Field(None, ge=1000, le=2100, example=2008)
    genre: Optional[str] = Field(None, example="Technology")


class BookResponse(BaseModel):
    """What the API returns for a single book."""
    id: int
    title: str
    author: str
    year: int
    genre: Optional[str]


# ── Routes ───────────────────────────────────────────────────────────────────

@app.get("/", tags=["Root"])
def root():
    """Health-check / welcome endpoint."""
    return {
        "message": "Welcome to the Books API!",
        "docs": "/docs",
        "endpoints": [
            "GET    /books          — list all books (supports ?genre= filter)",
            "GET    /books/{id}     — get a single book",
            "POST   /books          — create a new book",
            "PUT    /books/{id}     — fully replace a book",
            "PATCH  /books/{id}     — partially update a book",
            "DELETE /books/{id}     — delete a book",
        ],
    }


# ── GET (collection) ─────────────────────────────────────────────────────────
@app.get("/books", response_model=list[BookResponse], tags=["Books"])
def list_books(
    genre: Optional[str] = Query(None, description="Filter books by genre"),
):
    """
    **GET /books** — Retrieve all books.

    - Optionally filter by `?genre=Technology`
    - Returns an empty list if no books exist yet.
    """
    books = load_books()
    result = [{"id": int(k), **v} for k, v in books.items()]

    if genre:
        result = [b for b in result if (b.get("genre") or "").lower() == genre.lower()]

    return result


# ── GET (single) ─────────────────────────────────────────────────────────────
@app.get("/books/{book_id}", response_model=BookResponse, tags=["Books"])
def get_book(book_id: int = Path(..., description="ID of the book to retrieve")):
    """
    **GET /books/{book_id}** — Retrieve a single book by ID.

    Returns `404` if the book does not exist.
    """
    books = load_books()
    book = books.get(str(book_id))
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    return {"id": book_id, **book}


# ── POST ──────────────────────────────────────────────────────────────────────
@app.post("/books", response_model=BookResponse, status_code=201, tags=["Books"])
def create_book(payload: BookCreate):
    """
    **POST /books** — Create a new book.

    - ID is assigned automatically.
    - Returns `201 Created` with the new book.
    """
    books = load_books()
    book_id = next_id(books)
    books[str(book_id)] = payload.model_dump()
    save_books(books)
    return {"id": book_id, **payload.model_dump()}


# ── PUT ───────────────────────────────────────────────────────────────────────
@app.put("/books/{book_id}", response_model=BookResponse, tags=["Books"])
def replace_book(
    payload: BookUpdate,
    book_id: int = Path(..., description="ID of the book to replace"),
):
    """
    **PUT /books/{book_id}** — Fully replace a book.

    - Every field must be provided (full replacement).
    - Returns `404` if the book does not exist.
    """
    books = load_books()
    if str(book_id) not in books:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    books[str(book_id)] = payload.model_dump()
    save_books(books)
    return {"id": book_id, **payload.model_dump()}


# ── PATCH ─────────────────────────────────────────────────────────────────────
@app.patch("/books/{book_id}", response_model=BookResponse, tags=["Books"])
def update_book(
    payload: BookPatch,
    book_id: int = Path(..., description="ID of the book to update"),
):
    """
    **PATCH /books/{book_id}** — Partially update a book.

    - Send only the fields you want to change.
    - Returns `404` if the book does not exist.
    """
    books = load_books()
    if str(book_id) not in books:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")

    existing = books[str(book_id)]
    # Merge: only overwrite fields that were explicitly sent
    updates = payload.model_dump(exclude_unset=True)
    existing.update(updates)
    books[str(book_id)] = existing
    save_books(books)
    return {"id": book_id, **existing}


# ── DELETE ────────────────────────────────────────────────────────────────────
@app.delete("/books/{book_id}", status_code=204, tags=["Books"])
def delete_book(book_id: int = Path(..., description="ID of the book to delete")):
    """
    **DELETE /books/{book_id}** — Delete a book.

    - Returns `204 No Content` on success.
    - Returns `404` if the book does not exist.
    """
    books = load_books()
    if str(book_id) not in books:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    del books[str(book_id)]
    save_books(books)
    # 204 → no response body
