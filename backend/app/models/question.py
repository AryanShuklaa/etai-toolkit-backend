from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(String(255), primary_key=True, index=True)
    question_text = Column(String(255), nullable=False)
    rule_id = Column(String(255), ForeignKey("rules.id"))
    ai_pipeline_stage = Column(String(255), nullable=False)
    priority = Column(String(50), nullable=False)

    rule = relationship("Rule", back_populates="questions")
