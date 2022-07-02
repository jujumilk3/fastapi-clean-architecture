from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routes import routers
from app.core.config import settings
from app.core.container import Container
from app.utils.class_object import singleton


@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=settings.PROJECT_NAME,
            openapi_url=f'{settings.API_V1_STR}/openapi.json',
            version='0.0.1'
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        self.db.create_database()

        # set cors
        if settings.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=['*'],
                allow_headers=['*'],
            )

        # set routes
        @self.app.get('/')
        def root():
            return "service is working"

        self.app.include_router(routers, prefix=settings.API_V1_STR)


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
