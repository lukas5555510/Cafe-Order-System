from fastapi import APIRouter
from src.app.schemas.common import ResponseModel

router = APIRouter()


@router.get("/", response_model = ResponseModel[dict])
async def root():
    return ResponseModel(status = "succeed", code=200, message="hello world endpoint", data={"message": "Hello World"})