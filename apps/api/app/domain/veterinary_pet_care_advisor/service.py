from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.veterinary_pet_care_advisor.models import AgenticVeterinaryPetCareAdvisorSession, AgenticVeterinaryPetCareAdvisorItem
from app.domain.veterinary_pet_care_advisor.schemas import AgenticVeterinaryPetCareAdvisorSessionCreate, AgenticVeterinaryPetCareAdvisorItemCreate

class AgenticVeterinaryPetCareAdvisorService:
    @staticmethod
    def create_session(db: Session, data: AgenticVeterinaryPetCareAdvisorSessionCreate) -> AgenticVeterinaryPetCareAdvisorSession:
        db_obj = AgenticVeterinaryPetCareAdvisorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticVeterinaryPetCareAdvisorSession:
        return db.query(AgenticVeterinaryPetCareAdvisorSession).filter(AgenticVeterinaryPetCareAdvisorSession.id == session_id).first()
