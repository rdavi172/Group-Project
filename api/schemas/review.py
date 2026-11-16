from pydantic import BaseModel, Field
from typing import Optional


class ReviewBase(BaseModel):
    score: int = Field(..., ge=1, le=5, description="Rating score from 1 to 5")
    review_text: Optional[str] = None


class ReviewCreate(ReviewBase):
    customer_id: int


class ReviewResponse(ReviewBase):
    review_id: int
    customer_id: int

    class Config:
        from_attributes = True