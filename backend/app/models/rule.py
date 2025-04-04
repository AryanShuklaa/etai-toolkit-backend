from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(String(255), primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    category = Column(String(255), default="")
    ai_stage = Column(String(255), default="")

    # Relationship to the questions
    questions = relationship("Question", back_populates="rule")

    def __repr__(self):
        return f"<Rule(id={self.id}, title={self.title})>"
