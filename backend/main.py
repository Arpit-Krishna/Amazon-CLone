from fastapi import FastAPI,Body
from fastapi.middleware import cors
from fastapi.middleware.cors import CORSMiddleware

import amzon
import auth
app = FastAPI()
origins=[
    "https://localhost:3000",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(amzon.router)

app.include_router(auth.router)

@app.get('/')
def greet():
    return "3rd year elite intro to fastapi"