from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database
from app.services.recommender import recommend_items

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@router.get("/{user_id}")
def recommend(user_id: int, db: Session = Depends(database.get_db)):
    return recommend_items(user_id, db)

