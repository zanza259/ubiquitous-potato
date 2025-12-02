from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Boolean,
    DateTime,
    CheckConstraint,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from potato.storage.models import Group, Kitchen, User, Recipe, Audit

Base = declarative_base()


class PotatoGroup(Base):
    __tablename__ = "potato_group"

    group_id = Column(String, primary_key=True)
    display_name = Column(String, nullable=False)

    kitchens = relationship("PotatoKitchen", back_populates="group")

    def to_model(self) -> Group:
        return Group(group_id=self.group_id, display_name=self.display_name)

    @staticmethod
    def from_model(model: Group) -> "PotatoGroup":
        return PotatoGroup(group_id=model.group_id, display_name=model.display_name)


class PotatoKitchen(Base):
    __tablename__ = "potato_kitchen"

    kitchen_id = Column(String, primary_key=True)
    group_id = Column(String, ForeignKey("potato_group.group_id"), nullable=False)
    display_name = Column(String, nullable=False)

    group = relationship("PotatoGroup", back_populates="kitchens")
    users = relationship("PotatoUser", back_populates="kitchen")

    def to_model(self) -> Kitchen:
        return Kitchen(
            kitchen_id=self.kitchen_id,
            group_id=self.group_id,
            display_name=self.display_name,
        )

    @staticmethod
    def from_model(model: Kitchen) -> "PotatoKitchen":
        return PotatoKitchen(
            kitchen_id=model.kitchen_id,
            group_id=model.group_id,
            display_name=model.display_name,
        )


class PotatoUser(Base):
    __tablename__ = "potato_user"

    user_id = Column(String, primary_key=True)
    kitchen_id = Column(String, ForeignKey("potato_kitchen.kitchen_id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    kitchen = relationship("PotatoKitchen", back_populates="users")
    recipes_created = relationship(
        "PotatoRecipe", foreign_keys="PotatoRecipe.created_by", back_populates="creator"
    )
    recipes_modified = relationship(
        "PotatoRecipe",
        foreign_keys="PotatoRecipe.last_modified_by",
        back_populates="modifier",
    )
    audits = relationship("PotatoAudit", back_populates="user")

    def to_model(self) -> User:
        return User(
            user_id=self.user_id,
            kitchen_id=self.kitchen_id,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    @staticmethod
    def from_model(model: User) -> "PotatoUser":
        return PotatoUser(
            user_id=model.user_id,
            kitchen_id=model.kitchen_id,
            first_name=model.first_name,
            last_name=model.last_name,
        )


class PotatoRecipe(Base):
    __tablename__ = "potato_recipe"

    recipe_id = Column(String, primary_key=True)
    version = Column(Integer, nullable=False)
    state = Column(String, nullable=False, default="DRAFT")
    latest = Column(Boolean, nullable=False, default=True)
    cuisine = Column(String, nullable=True)
    description = Column(String, nullable=True)
    yield_amount = Column(Float, nullable=True, name="yield")
    ingredients = Column(String, nullable=False)  # JSON blob
    instructions = Column(String, nullable=False)  # JSON blob
    created_by = Column(String, ForeignKey("potato_user.user_id"), nullable=False)
    created_timestamp = Column(DateTime, nullable=False)
    last_modified_by = Column(String, ForeignKey("potato_user.user_id"), nullable=False)
    last_modified_timestamp = Column(DateTime, nullable=False)

    __table_args__ = (CheckConstraint("state IN ('DRAFT', 'PUBLISHED', 'ARCHIVED')"),)

    creator = relationship(
        "PotatoUser", foreign_keys=[created_by], back_populates="recipes_created"
    )
    modifier = relationship(
        "PotatoUser", foreign_keys=[last_modified_by], back_populates="recipes_modified"
    )
    audits = relationship("PotatoAudit", back_populates="recipe")

    def to_model(self) -> Recipe:
        return Recipe(
            recipe_id=self.recipe_id,
            version=self.version,
            state=self.state,
            latest=self.latest,
            cuisine=self.cuisine,
            description=self.description,
            yield_amount=self.yield_amount,
            ingredients=self.ingredients,
            instructions=self.instructions,
            created_by=self.created_by,
            created_timestamp=self.created_timestamp,
            last_modified_by=self.last_modified_by,
            last_modified_timestamp=self.last_modified_timestamp,
        )

    @staticmethod
    def from_model(model: Recipe) -> "PotatoRecipe":
        return PotatoRecipe(
            recipe_id=model.recipe_id,
            version=model.version,
            state=model.state,
            latest=model.latest,
            cuisine=model.cuisine,
            description=model.description,
            yield_amount=model.yield_amount,
            ingredients=model.ingredients,
            instructions=model.instructions,
            created_by=model.created_by,
            created_timestamp=model.created_timestamp,
            last_modified_by=model.last_modified_by,
            last_modified_timestamp=model.last_modified_timestamp,
        )


class PotatoAudit(Base):
    __tablename__ = "potato_audit"

    audit_id = Column(String, primary_key=True)
    recipe_id = Column(String, ForeignKey("potato_recipe.recipe_id"), nullable=False)
    action = Column(String, nullable=False)
    action_by = Column(String, ForeignKey("potato_user.user_id"), nullable=False)
    action_timestamp = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)

    __table_args__ = (
        CheckConstraint("action IN ('CREATE', 'ARCHIVE', 'UNARCHIVE', 'EDIT')"),
    )

    recipe = relationship("PotatoRecipe", back_populates="audits")
    user = relationship("PotatoUser", back_populates="audits")

    def to_model(self) -> Audit:
        return Audit(
            audit_id=self.audit_id,
            recipe_id=self.recipe_id,
            action=self.action,
            timestamp=self.action_timestamp,
            user_id=self.action_by,
        )

    @staticmethod
    def from_model(model: Audit) -> "PotatoAudit":
        return PotatoAudit(
            audit_id=model.audit_id,
            recipe_id=model.recipe_id,
            action=model.action,
            action_by=model.user_id,
            action_timestamp=model.timestamp,
        )
