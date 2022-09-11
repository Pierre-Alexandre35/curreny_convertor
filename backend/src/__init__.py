from fastapi import FastAPI, Depends


def create_app() -> FastAPI:
    root_app = FastAPI()

    @root_app.get("/")
    async def root():
        return {"message": "Hello World"}

    return root_app
