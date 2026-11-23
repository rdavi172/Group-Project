from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    promo_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)

    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_number = Column(String(100), unique=True, nullable=False)
    order_status = Column(String(50), nullable=False, default="Pending")
    total_price = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    order_type = Column(String(50), nullable=False)

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)