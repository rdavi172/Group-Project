from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True