#*******************************************************************************#
# Fecha Creación:  24 Marzo 2021.                                               #
# Autor:           Iván Fonseca Castro                                          #
#                                                                               #
# Descripción:     Modelo para las entidades que componen el Proyecto del       #
#                  Star Wars Blog                                               #
#*******************************************************************************#

import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# Definición de Tipo de Dato Personalizado para identificar las entidades principales
class EntityTypeEnum(enum.Enum):
    person = 1
    planet = 2
    vehicle = 3

# INICIO - Definición de Tablas para Cátalogos
# [hair_color_cat] : Esta entidad permitirá almacenar un Cátalogo de Color de Pelo
class HairColorCat(Base):
    __tablename__ = 'hair_color_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# [skin_color_cat] : Esta entidad permitirá almacenar un Cátalogo de Color de Piel
class SkinColorCat(Base):
    __tablename__ = 'skin_color_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# [eye_color_cat] : Esta entidad permitirá almacenar un Cátalogo de Color de Ojos
class EyeColorCat(Base):
    __tablename__ = 'eye_color_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# [gender_cat] : Esta entidad permitirá almacenar un Cátalogo de Generos
class GenderCat(Base):
    __tablename__ = 'gender_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# [climate_cat] : Esta entidad permitirá almacenar un Cátalogo de Climas
class ClimateCat(Base):
    __tablename__ = 'climate_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# [terrain_cat] : Esta entidad permitirá almacenar un Cátalogo de Terrenos
class TerrainCat(Base):
    __tablename__ = 'terrain_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# [vehicle_class_cat] : Esta entidad permitirá almacenar un Cátalogo de Clases de Vehiculos
class VehicleClassCat(Base):
    __tablename__ = 'vehicle_class_cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
# FIN - Definición de Tablas para Cátalogos

# Definición de Entidades Principales
# [user] : Esta entidad permitirá almacenar los usuarios.
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    first_surname = Column(String(100), nullable=False)
    second_surname = Column(String(100))
    email = Column(String(250), unique=True)
    user_name = Column(String(50), unique=True)
    password = Column(String(50))
    user_image = Column(String(2000))
    gender_cat_id = Column(Integer, ForeignKey('gender_cat.id'))
    gender_cat = relationship(GenderCat)

# [people] : Esta entidad permitirá almacenar los personas o personajes.
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Date)
    height = Column(Integer)
    mass = Column(Integer)
    people_image = Column(String(2000))
    hair_color_cat_id = Column(Integer, ForeignKey('hair_color_cat.id'))
    hair_color_cat = relationship(HairColorCat)
    skin_color_cat_id = Column(Integer, ForeignKey('skin_color_cat.id'))
    skin_color_cat = relationship(SkinColorCat)
    eye_color_cat_id = Column(Integer, ForeignKey('eye_color_cat.id'))
    eye_color_cat = relationship(EyeColorCat)
    gender_cat_id = Column(Integer, ForeignKey('gender_cat.id'))
    gender_cat = relationship(GenderCat)

# [planet] : Esta entidad permitirá almacenar los planetas.
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer) 
    diameter = Column(Integer)
    gravity = Column(String(50))
    surface_water = Column(Integer)
    population = Column(Integer)
    planet_image = Column(String(2000))
    climate_cat_id = Column(Integer, ForeignKey('climate_cat.id'))
    climate_cat = relationship(ClimateCat)
    terrain_cat_id = Column(Integer, ForeignKey('terrain_cat.id'))
    terrain_cat = relationship(TerrainCat)

# [vehicle] : Esta entidad permitirá almacenar los personas o personajes.
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(100))
    manufacturer = Column(String(100)) 
    cost_in_credits = Column(Integer)
    length = Column(Float)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    vehicle_image = Column(String(2000))
    vehicle_class_cat_id = Column(Integer, ForeignKey('vehicle_class_cat.id'))
    vehicle_class_cat = relationship(VehicleClassCat)

# [favorite] : Esta entidad permitirá almacenar los favoritos
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favorite_id = Column(Integer, nullable=False)
    favorite_type = Column(Enum(EntityTypeEnum), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')