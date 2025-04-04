from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import rules, users, auth

app = FastAPI()

# Enable CORS (update allow_origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rules.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}
