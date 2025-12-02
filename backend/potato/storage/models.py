from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Group(BaseModel):
    group_id: str
    display_name: str


class Kitchen(BaseModel):
    kitchen_id: str
    group_id: str
    display_name: str


class User(BaseModel):
    user_id: str
    kitchen_id: str
    first_name: str
    last_name: str


class Recipe(BaseModel):
    recipe_id: str
    version: int
    state: str = Field(default="DRAFT")
    latest: bool = Field(default=True)
    cuisine: Optional[str] = None
    description: Optional[str] = None
    yield_amount: Optional[float] = Field(default=None, alias="yield")
    ingredients: str  # JSON blob
    instructions: str  # JSON blob
    created_by: str
    created_timestamp: datetime
    last_modified_by: str
    last_modified_timestamp: datetime


class Audit(BaseModel):
    audit_id: str
    recipe_id: str
    action: str
    timestamp: datetime
    user_id: str
