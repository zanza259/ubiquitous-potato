from fastapi import APIRouter, HTTPException, Request
from typing import Final
from potato.storage.db import StorageDB
from sqlalchemy import or_
import uuid
from datetime import datetime


from potato.models import ServiceSettings
from potato.storage.models import Recipe
from potato.storage.orm import PotatoRecipe

API_MODULE_ID: Final[str] = "recipe"


class RecipeAPI:
    def __init__(self, settings: ServiceSettings, storage_db: StorageDB) -> None:
        self._settings = settings
        self._storage_db = storage_db

        self._router = APIRouter()
        self._init_routes()

    @property
    def router(self) -> APIRouter:
        return self._router

    def _init_routes(self) -> None:
        self.router.add_api_route(
            "/recipes",
            self.list_recipes,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/recipes/search",
            self.search_recipes,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/recipe",
            self.create_recipe,
            methods=["POST"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/recipe/{recipe_id}",
            self.get_recipe,
            methods=["GET"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/recipe/{recipe_id}",
            self.update_recipe,
            methods=["POST"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/recipe/{recipe_id}/archive",
            self.archive_recipe,
            methods=["POST"],
            tags=[API_MODULE_ID],
        )

        self.router.add_api_route(
            "/recipe/{recipe_id}/unarchive",
            self.unarchive_recipe,
            methods=["POST"],
            tags=[API_MODULE_ID],
        )

    async def list_recipes(self) -> list[Recipe]:
        recipes: list[Recipe] = []

        with self._storage_db.new_session() as session:
            orm_recipes = (
                session.query(PotatoRecipe)
                .filter(PotatoRecipe.latest == True)
                .order_by(PotatoRecipe.created_timestamp.desc())
                .all()
            )

            recipes = [orm_recipe.to_model() for orm_recipe in orm_recipes]

        return recipes

    async def search_recipes(
        self, query_string: str, page: int, page_size: int = 100
    ) -> list[Recipe]:
        q = f"%{query_string}%"

        with self._storage_db.new_session() as session:
            orm_recipes = (
                session.query(PotatoRecipe)
                .filter(
                    PotatoRecipe.latest == True,
                    or_(
                        PotatoRecipe.description.ilike(q),
                        PotatoRecipe.ingredients.ilike(q),
                        PotatoRecipe.instructions.ilike(q),
                    ),
                )
                .order_by(PotatoRecipe.created_timestamp.desc())
                .offset(page * page_size)
                .limit(page_size)
                .all()
            )

            return [orm_recipe.to_model() for orm_recipe in orm_recipes]

    async def create_recipe(self, request: Request) -> Recipe:
        raw_json = await request.json()

        new_recipe = Recipe(
            recipe_id=str(uuid.uuid4()),
            version=1,
            state="DRAFT",
            latest=True,
            cuisine=raw_json.get("cuisine", "unknown"),
            description=raw_json.get("description", "no description"),
            yield_amount=raw_json.get("yield", 0.0),
            ingredients=raw_json.get("ingredients", "[]"),
            instructions=raw_json.get("instructions", "[]"),
            created_by=raw_json.get("created_by", "system"),
            created_timestamp=datetime.now(),
            last_modified_by=raw_json.get("created_by", "system"),
            last_modified_timestamp=datetime.now(),
        )

        with self._storage_db.new_session() as session:
            orm_recipe = PotatoRecipe.from_model(new_recipe)
            session.add(orm_recipe)
            session.commit()

        return new_recipe

    async def get_recipe(self, recipe_id: str) -> Recipe:
        with self._storage_db.new_session() as session:
            orm_recipe = (
                session.query(PotatoRecipe)
                .filter(PotatoRecipe.recipe_id == recipe_id)
                .first()
            )

            if orm_recipe is None:
                raise HTTPException(status_code=404, detail="Recipe not found")

            return orm_recipe.to_model()

    async def update_recipe(self, recipe_id: str, request: Request) -> Recipe:
        raw_json = await request.json()

        with self._storage_db.new_session() as session:
            # Fetch the latest version of this recipe
            orm_recipe = (
                session.query(PotatoRecipe)
                .filter(
                    PotatoRecipe.recipe_id == recipe_id,
                    PotatoRecipe.latest == True,
                )
                .first()
            )

            if orm_recipe is None:
                raise HTTPException(status_code=404, detail="Recipe not found")

            # Mark the old version as not latest
            orm_recipe.latest = False

            # Create new archived version
            new_version = orm_recipe.version + 1

            archived_copy = PotatoRecipe(
                recipe_id=orm_recipe.recipe_id,
                version=new_version,
                state="ARCHIVED",
                latest=False,  # archived versions are not latest
                cuisine=raw_json.get("cuisine", orm_recipe.cuisine),
                description=raw_json.get("description", orm_recipe.description),
                yield_amount=raw_json.get("yield", orm_recipe.yield_amount),
                ingredients=raw_json.get("ingredients", orm_recipe.ingredients),
                instructions=raw_json.get("instructions", orm_recipe.instructions),
                created_by=orm_recipe.created_by,
                created_timestamp=orm_recipe.created_timestamp,
                last_modified_by=raw_json.get(
                    "modified_by", orm_recipe.last_modified_by
                ),
                last_modified_timestamp=datetime.now(),
            )

            session.add(archived_copy)
            session.commit()

        return archived_copy.to_model()

    async def archive_recipe(self, recipe_id: str) -> Recipe:
        with self._storage_db.new_session() as session:
            # Fetch the latest version of this recipe
            orm_recipe = (
                session.query(PotatoRecipe)
                .filter(
                    PotatoRecipe.recipe_id == recipe_id,
                    PotatoRecipe.latest == True,
                    PotatoRecipe.state != "ARCHIVED",
                )
                .first()
            )

            if orm_recipe is None:
                raise HTTPException(status_code=404, detail="Recipe not found")

            # Mark the old version as not latest
            orm_recipe.latest = False

            # Create new archived version
            new_version = orm_recipe.version + 1

            updated_recipe = PotatoRecipe(
                recipe_id=orm_recipe.recipe_id,
                version=new_version,
                state="ARCHIVED",
                latest=True,
                cuisine=orm_recipe.cuisine,
                description=orm_recipe.description,
                yield_amount=orm_recipe.yield_amount,
                ingredients=orm_recipe.ingredients,
                instructions=orm_recipe.instructions,
                created_by=orm_recipe.created_by,
                created_timestamp=orm_recipe.created_timestamp,
                last_modified_by="system",  # In real implementation, get from auth context
                last_modified_timestamp=datetime.now(),
            )

            session.add(updated_recipe)
            session.commit()

        return updated_recipe.to_model()

    async def unarchive_recipe(self, recipe_id: str) -> Recipe:
        with self._storage_db.new_session() as session:
            # Fetch the latest version of this recipe
            orm_recipe = (
                session.query(PotatoRecipe)
                .filter(
                    PotatoRecipe.recipe_id == recipe_id,
                    PotatoRecipe.latest == True,
                    PotatoRecipe.state == "ARCHIVED",
                )
                .first()
            )

            if orm_recipe is None:
                raise HTTPException(status_code=404, detail="Recipe not found")

            # Mark the old version as not latest
            orm_recipe.latest = False

            # Create new archived version
            new_version = orm_recipe.version + 1

            updated_recipe = PotatoRecipe(
                recipe_id=orm_recipe.recipe_id,
                version=new_version,
                state="PUBLISHED",
                latest=False,  # archived versions are not latest
                cuisine=orm_recipe.cuisine,
                description=orm_recipe.description,
                yield_amount=orm_recipe.yield_amount,
                ingredients=orm_recipe.ingredients,
                instructions=orm_recipe.instructions,
                created_by=orm_recipe.created_by,
                created_timestamp=orm_recipe.created_timestamp,
                last_modified_by="system",  # In real implementation, get from auth context
                last_modified_timestamp=datetime.now(),
            )

            session.add(updated_recipe)
            session.refresh(updated_recipe)
            session.commit()

        return updated_recipe.to_model()
