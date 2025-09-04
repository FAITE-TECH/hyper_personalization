from sqlalchemy.orm import Session
from app import models

EVENT_WEIGHTS = {
    models.EventType.view: 0.5,
    models.EventType.play: 0.7,
    models.EventType.like: 1.0,
    models.EventType.rate: 1.2,
    models.EventType.purchase: 1.5,
}

def recommend_items(user_id: int, db: Session):
    interactions = db.query(models.Interaction).filter(models.Interaction.user_id == user_id).all()
    scores = {}

    for interaction in interactions:
        weight = EVENT_WEIGHTS[interaction.event_type]
        if interaction.event_type == models.EventType.rate and interaction.rating:
            weight += interaction.rating / 5.0  
        scores[interaction.item_id] = scores.get(interaction.item_id, 0) + weight

    ranked_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    recommended_ids = [item_id for item_id, _ in ranked_items]

    recommended_items = db.query(models.Item).filter(models.Item.id.in_(recommended_ids)).all()
    items_data = [
        {
            "id": item.id,
            "title": item.title,
            "type": item.type,
            "tags": item.tags,
            "item_metadata": item.item_metadata
        }
        for item in recommended_items
    ]

    return {"user_id": user_id, "recommended_items": items_data}
