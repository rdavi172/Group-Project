from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    amount = Column(Integer, index=True, nullable=False)
    subtotal = Column(DECIMAL(10, 2), nullable=False)
    special_instructions = Column(String(300), nullable=True)

    menu_item = relationship("MenuItem", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")