from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/interactions", tags=["Interactions"])

@router.post("/", response_model=schemas.Interaction)
def create_interaction(interaction: schemas.InteractionCreate, db: Session = Depends(database.get_db)):
    db_interaction = models.Interaction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

@router.get("/", response_model=list[schemas.Interaction])
def list_interactions(db: Session = Depends(database.get_db)):
    return db.query(models.Interaction).all()
