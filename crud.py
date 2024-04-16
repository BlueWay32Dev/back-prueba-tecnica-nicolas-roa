from sqlalchemy.orm import Session
import models
import schemas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.TaskBase(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TaskBase).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(models.TaskBase).filter(models.TaskBase.id == task_id).first()

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = db.query(models.TaskBase).filter(models.TaskBase.id == task_id).first()
    if db_task:
        for var, value in task.dict().items():
            setattr(db_task, var, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.TaskBase).filter(models.TaskBase.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
