from sqlalchemy import Column, ForeignKey, Integer, Text, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)

    review_text = Column(Text, nullable=True)
    score = Column(Integer, nullable=False)  # e.g., 1 to 5
    created_at = Column(DATETIME, nullable=False, server_default=func.now())

    # Relationships
    customer = relationship("Customer", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")
