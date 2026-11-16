from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    ingredient: Optional[str] = None
    amount: int
    unit: str



class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    ingredient: Optional[str] = None
    amount: Optional[int] = None
    unit: Optional[str] = None


class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True
