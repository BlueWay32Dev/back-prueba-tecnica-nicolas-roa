from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import schemas
import crud
import database
from database import Base

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# Configurar los orígenes permitidos (cambia "*" a tus orígenes permitidos)
origins = ["*"]

# Agregar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=database.engine)

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate):
    return crud.create_task(db=database.SessionLocal(), task=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10):
    return crud.get_tasks(db=database.SessionLocal(), skip=skip, limit=limit)

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int):
    db_task = crud.get_task(db=database.SessionLocal(), task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate):
    updated_task = crud.update_task(db=database.SessionLocal(), task_id=task_id, task=task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return updated_task

@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int):
    deleted_task = crud.delete_task(db=database.SessionLocal(), task_id=task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
