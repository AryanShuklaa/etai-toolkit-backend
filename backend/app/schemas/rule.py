from pydantic import BaseModel
from typing import Optional

class RuleBase(BaseModel):
    title: str
    description: str
    category: Optional[str] = ""
    ai_stage: Optional[str] = ""

class RuleCreate(RuleBase):
    pass

class Rule(RuleBase):
    id: str

    class Config:
        orm_mode = True
