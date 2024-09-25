from typing import Union, List, Dict, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#
#
# # class UserSchema(BaseModel):
# #     name: str
# #     age: int
#
#
# class ResponseSchema(BaseModel):
#     test: Optional[str] = None # UserSchema
#     id: int
#
#
# @app.get('/test/{id}')
# async def test_function(
#         id: int,
#         query: int,
#
# ) -> ResponseSchema:
#     return {
#         "test": "test",
#         "id": 123,
#     }
#
#
# class TestSchema(BaseModel):
#     login: str
#     password: str
#
#
# @app.post('/test')
# async def test_post_request(data: ResponseSchema):
#     print(data)
#     return {
#         "login"
#     }


tasks = [
    {
        "id": 1,
        "description": "do homework 1"
    },
    {
        "id": 2,
        "description": "do homework 2"
    },
    {
        "id": 3,
        "description": "do homework 3"
    },
    {
        "id": 4,
        "description": "do homework 4"
    },
]


@app.get('/tasks/')
@app.get('/tasks/{id}', name='get task by id')
async def get_tasks(
        id: int = None
):
    if id is not None:
        task = list(filter(lambda x: x['id'] == id, tasks))
        return {"task": task[0] if task else None}
    return {"tasks": tasks}


class TaskSchema(BaseModel):
    id: int
    description: str


@app.post('/tasks/')
async def create_task(data: TaskSchema):
    tasks.append({"id": data.id, "description": data.description})
    print(tasks)
    return {"data": data}


class TaskUpdateSchema(BaseModel):
    description: str


@app.post('/update-task/{id}')
async def update_task(id: int, data: TaskUpdateSchema):
    for task in tasks:
        if task["id"] == id:
            task["description"] = data.description
            return {
                "update task": task
            }

    return {
        "task": "undefined"
    }




