from dependency_injector import containers, providers

from app.core.database import Database
from app.core.config import settings

from app.repositories import *
from app.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'app.api.v1.endpoints.user',
            'app.api.v1.endpoints.user',
        ]
    )

    db = providers.Singleton(Database, db_url=settings.DATABASE_URI)

    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    user_service = providers.Factory(UserService, user_repository=user_repository)
