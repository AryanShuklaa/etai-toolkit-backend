from sqlalchemy import Column, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(255), primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
