from app.database import engine
from app.database import Base

Base.metadata.create_all(bind=engine)
 
