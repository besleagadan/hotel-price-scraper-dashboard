from sqlalchemy import Column, Integer, String, Date, Numeric, TIMESTAMP, text
from db.connect import Base

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    date = Column(Date, nullable=False)
    price = Column(Numeric, nullable=False)
    source = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
