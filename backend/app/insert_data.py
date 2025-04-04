from app.database import SessionLocal
from app.models.rule import Rule
from app.models.question import Question

def insert_sample_data():
    db = SessionLocal()

    # Sample rules
    rules = [
        Rule(
            id="IF-001", 
            title="Clearly Defined Purpose and Scope", 
            description="The system must have a documented and communicated purpose, target users and operational scope.",
            category="",
            ai_stage=""
        ),
        Rule(
            id="IF-002", 
            title="Specification of Functional Boundaries", 
            description="Assumptions, constraints and known unsupported conditions must be documented.",
            category="",
            ai_stage=""
        ),
        Rule(
            id="IF-003", 
            title="Verification Against Intended Use Cases", 
            description="System behavior must be tested against intended real-world scenarios.",
            category="",
            ai_stage=""
        ),
    ]
    db.add_all(rules)
    db.commit()

    # Sample questions
    questions = [
        Question(
            id="Q1.1", 
            rule_id="IF-001", 
            question_text="Has the system’s intended purpose been clearly documented and agreed upon with stakeholders?", 
            ai_pipeline_stage="Problem Formulation", 
            priority="High"
        ),
        Question(
            id="Q1.2", 
            rule_id="IF-001", 
            question_text="Are the target users, usage conditions and deployment goals defined?", 
            ai_pipeline_stage="Problem Formulation", 
            priority="High"
        ),
        Question(
            id="Q2.1", 
            rule_id="IF-002", 
            question_text="Are functional limitations, assumptions and unsupported scenarios documented?", 
            ai_pipeline_stage="Design Specification", 
            priority="High"
        ),
        Question(
            id="Q2.2", 
            rule_id="IF-002", 
            question_text="Are constraints communicated to end-users or integrators?", 
            ai_pipeline_stage="Deployment Planning", 
            priority="Medium"
        ),
    ]
    db.add_all(questions)
    db.commit()
    print("✅ Sample rules and questions inserted successfully!")
    db.close()

if __name__ == "__main__":
    insert_sample_data()
