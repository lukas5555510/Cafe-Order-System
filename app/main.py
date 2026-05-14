from fastapi import FastAPI, APIRouter
from app.api.router import router

def create_app():
    app = FastAPI(
        title="Cafe-Order-System",
    )

    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)