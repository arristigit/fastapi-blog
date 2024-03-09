from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    description: str

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/blo")
async def blo(id: bool=True, s: Optional[str]=None):
    return {"data": id, "s": s}

@app.post("/blog")
async def blog(blog: Blog):
    # return blog
    print(blog)
    return {"data": blog}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) #, reload=True)
    # uvicorn.run("app:index", host="127.0.0.1", port=9000) #, reload=True)