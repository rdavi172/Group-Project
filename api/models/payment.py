from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)

    card_information = Column(String(100), nullable=True)  # e.g., masked card / last 4 digits
    transaction_status = Column(String(50), nullable=False, default="Pending")
    payment_type = Column(String(50), nullable=False)  # e.g., "Credit Card", "Debit", "Cash"
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DATETIME, nullable=False, server_default=func.now())

    # Relationships
    order = relationship("Order", back_populates="payment")
