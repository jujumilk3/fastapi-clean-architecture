import os

from dotenv import load_dotenv
from typing import Any, Dict, List, Optional
from pydantic import BaseSettings, validator

load_dotenv()

ENV_DATABASE_MAPPER = {
    'prod': 'fca',
    'staging': 'fca-staging',
    'dev': 'fca-dev',
    'test': 'fca-test'
}


class Settings(BaseSettings):
    # base
    ENV: str = os.getenv('ENV', 'dev')
    API_V1_STR: str = '/api/v1'
    API_V2_STR: str = '/api/v2'
    PROJECT_NAME: str = 'fca-api'
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # date
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
    DATE_FORMAT = '%Y-%m-%d'

    # auth
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    # database
    MYSQL_USER: str = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST: str = os.getenv('MYSQL_HOST')
    MYSQL_PORT: str = os.getenv('MYSQL_PORT', '3306')
    MYSQL_DATABASE: str = ENV_DATABASE_MAPPER.get(ENV, 'fca-dev')
    DATABASE_URI: Optional[str] = os.getenv('DATABASE_URI')

    @validator('DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql+pymysql://{values.get('MYSQL_USER')}:{values.get('MYSQL_PASSWORD')}@" \
               f"{values.get('MYSQL_HOST')}:{values.get('MYSQL_PORT')}/{values.get('MYSQL_DATABASE')}"

    # find query
    PAGE = 1
    PAGE_SIZE = 10
    ORDERING = '-id'

    class Config:
        case_sensitive = True


settings = Settings()
