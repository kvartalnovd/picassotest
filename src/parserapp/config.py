import os

from pathlib import Path

APP_NAME = 'ParserAPP'

PARSER_APP_DIR = Path(__file__).resolve().parent
CONTENT_DIR = PARSER_APP_DIR.joinpath('content')
LOG_DIR = PARSER_APP_DIR.parent.joinpath('storage', 'logs', 'parserapp')


# PostgreSQL Database
PG_HOST_NAME = os.environ.get("POSTGRES_HOST", None)
PG_DBNAME = os.environ.get("POSTGRES_DB", None)
PG_PORT = os.environ.get("POSTGRES_PORT", "5432")
PG_USERNAME = os.environ.get("POSTGRES_USER", "user")
PG_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")


# Init Data
INIT_SERVICE_CALL_DATA = CONTENT_DIR.joinpath('police-department-calls-for-service.csv.zip')
