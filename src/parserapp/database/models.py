from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    state_id = Column('state_id', Integer, primary_key=True)
    name = Column('name', String, unique=True)


class City(Base):
    __tablename__ = 'cities'

    city_id = Column('city_id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
    state = Column('state', Integer, ForeignKey("states.state_id"))


class AddressTypes(Base):
    __tablename__ = 'address_types'

    address_type_id = Column('address_type_id', Integer, primary_key=True)
    name = Column('name', String, unique=True)


class ServiceCall(Base):
    __tablename__ = 'service_calls'

    call_id = Column('call_id', Integer, primary_key=True)
    crime_id = Column('crime_id', Integer, unique=True)
    original_crime_type_name = Column('original_crime_type_name', String(255))
    report_date = Column('report_date', DateTime)
    offense_date = Column('offense_date', DateTime)
    call_date_time = Column('call_date_time', DateTime)
    disposition = Column('disposition', String(255))
    address = Column('address', String(255))
    city = Column('city', Integer, ForeignKey("cities.city_id"), nullable=True)
    address_type = Column('address_type', Integer, ForeignKey("address_types.address_type_id"))
    common_location = Column('common_location', String(255), nullable=True)
