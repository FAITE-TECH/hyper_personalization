from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, func, JSON
from sqlalchemy.orm import relationship
from .database import Base
import enum

class ItemType(str, enum.Enum):
    movie = "movie"
    music = "music"
    product = "product"

class EventType(str, enum.Enum):
    view = "view"
    play = "play"
    like = "like"
    rate = "rate"
    purchase = "purchase"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    interactions = relationship("Interaction", back_populates="user", cascade="all, delete-orphan")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    type = Column(Enum(ItemType), nullable=False)
    tags = Column(String, nullable=True)  # e.g. "thriller,serial-killer"
    item_metadata = Column("metadata", JSON, nullable=True)  # ✅ fixed reserved word
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    interactions = relationship("Interaction", back_populates="item", cascade="all, delete-orphan")

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    event_type = Column(Enum(EventType), nullable=False)
    rating = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="interactions")
    item = relationship("Item", back_populates="interactions")
