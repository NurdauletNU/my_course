from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool


todos = [
    {"id": 1, "title": "Погулять с собакой", "completed": False},
    {"id": 2, "title": "Приготовить обед", "completed": True},
]


@app.get("/todos", response_model=List[TodoItem])
async def read_todos():
    return todos


@app.post("/todos", response_model=TodoItem)
async def create_todo(title: str):
    new_todo = {"id": len(todos) + 1, "title": title, "completed": False}
    todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo_status(todo_id: int, completed: bool):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
