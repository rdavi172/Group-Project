from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promoCode: str
    ExpirationDate: datetime



class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promoCode: Optional[str] = None
    ExpirationDate: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
