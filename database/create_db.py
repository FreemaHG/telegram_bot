from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Проверить, где именно создается БД
engine = create_engine('sqlite:///hostels_db', connect_args={'check_same_thread': False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Locations(Base):
    """ Структурная таблица с сохранением локаций, их id и id их дочерних записей """
    __tablename__ = 'locations'

    # id локации - не может быть пустым, уникальное, автоматически НЕ заполняется
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=False)
    parent_id = Column(Integer, nullable=True)  # id родительской локации
    location = Column(String(200), nullable=False)  # Название локации
    # Адрес локации (для уточнения, т.к. встречаются локации с одинаковыми названиями)
    address = Column(String(400), nullable=False)
    type = Column(String(100), nullable=False)  # Тип локации (город, регион, соседи (районы, улицы) и т.п.)

    hotels = relationship('Hotels', backref='locations')  # Связь с таблицей "Hotels"


class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=False)
    id_location = Column(Integer, ForeignKey('locations.id'))  # Внешний ключ на id локации
    name = Column(String(300), nullable=False)
    address = Column(String(500), nullable=False)
    distance_to_center = Column(String(100), nullable=True)
    price = Column(Float, nullable=False)

    photos = relationship('Photos', backref='hotels')  # Связь с таблицей "Photos"


class Photos(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    id_hotel = Column(Integer, ForeignKey('hotels.id'))  # Внешний ключ на id отеля
    url = Column(String, nullable=False)
    type = Column(String(50), nullable=False)  # room / hotel
