from typing import Optional
from pydantic import BaseModel


class OrderDetailBase(BaseModel):
    order_id: int
    menu_item_id: int
    amount: int
    subtotal: float
    special_instructions: Optional[str] = None


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    amount: Optional[int] = None
    subtotal: Optional[float] = None
    special_instructions: Optional[str] = None


class OrderDetail(OrderDetailBase):
    id: int

    class ConfigDict:
        from_attributes = True