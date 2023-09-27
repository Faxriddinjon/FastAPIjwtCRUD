from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import blogs, users, auth, root
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)


app.include_router(root.router)
app.include_router(auth.router)
app.include_router(blogs.router)
app.include_router(users.router)