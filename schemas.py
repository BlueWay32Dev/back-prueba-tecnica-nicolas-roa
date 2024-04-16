from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    subTitle: str
    description: str
    priority: int
    status_id: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskDelete(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
