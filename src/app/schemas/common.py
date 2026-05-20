from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    status: str
    code: int
    message: str
    data: Optional[T] = None
    errors: Optional[List[dict]] = None
