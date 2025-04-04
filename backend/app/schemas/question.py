from pydantic import BaseModel

class QuestionBase(BaseModel):
    question_text: str
    rule_id: str
    ai_pipeline_stage: str
    priority: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: str

    class Config:
        orm_mode = True
