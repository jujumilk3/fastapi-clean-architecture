import os

from dotenv import load_dotenv

load_dotenv()

ENV: str = ""


class BaseConfigs:
    # base
    ENV: str = os.getenv("ENV", "test")
    API: str = "/api"
    API_V1_STR: str = "/api/v1"
    API_V2_STR: str = "/api/v2"
    PROJECT_NAME: str = "fca-api"

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # database
    DB_NAME: str = os.getenv("DB_NAME", "fca-test")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")

    DATABASE_URL: str = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )

    # find query
    PAGE = 1
    PAGE_SIZE = 20
    ORDERING = "-id"

    class Config:
        case_sensitive = True


class TestSettings(BaseConfigs):
    ENV: str = "test"


settings = BaseConfigs
configs = BaseConfigs

if ENV == "prod":
    pass
elif ENV == "stage":
    pass
elif ENV == "dev":
    configs = BaseConfigs
elif ENV == "test":
    configs = TestSettings
    setting = TestSettings
