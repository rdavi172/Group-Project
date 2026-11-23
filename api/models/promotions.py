from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True)
    promoCode = Column(String(15), unique=True, index=True, nullable=False )
    ExpirationDate = Column(DATETIME)