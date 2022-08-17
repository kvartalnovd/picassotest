from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, Session


class PostgreSQL:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(PostgreSQL, cls).__new__(cls)
        return cls.__instance

    def __del__(self):
        self.close()
        PostgreSQL.__instance = None

    def __init__(self, container_name: str, dbname: str, username: str, password: str) -> None:
        self.__engine = PostgreSQL.create_engine_from_docker_container(
            username=username,
            password=password,
            container_name=container_name,
            dbname=dbname
        )
        self.__session = Session(self.__engine)

    @staticmethod
    def create_engine_from_docker_container(username: str, password: str, container_name: str, dbname: str):
        conn_url = f'postgresql+psycopg2://{username}:{password}@{container_name}/{dbname}'
        return create_engine(conn_url)

    def get_or_create(self, model, **kwargs):
        instance = self.__session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = model(**kwargs)
            self.__session.add(instance)
            self.__session.commit()
            return instance

    def create_if_not_exists(self, model, verification_field=None, **kwargs):
        verification_field_filter = dict(**kwargs) \
            if not verification_field \
            else {verification_field: kwargs.get(verification_field)}
        instance = self.__session.query(model).filter_by(**verification_field_filter).first()
        if not instance:
            instance = model(**kwargs)
            self.__session.add(instance)
            self.__session.commit()

    def close(self) -> None:
        self.__session.close()
