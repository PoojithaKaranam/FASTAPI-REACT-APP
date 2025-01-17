from fastapi import FastAPI
from routes.user import router as user_router
from routes.note import router as note_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(note_router, prefix="/note")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
