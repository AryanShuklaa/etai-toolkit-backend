from app.database import Base, engine
from app.models.rule import Rule
from app.models.question import Question
from app.models.user import User

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ MySQL Database Tables Created Successfully!")

if __name__ == "__main__":
    init_db()
