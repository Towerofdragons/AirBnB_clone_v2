#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models import storage_type


class Amenity(BaseModel, Base):
    """
    Amenity class that showcases the use of many-to-many
    relationships in sqlalchmey.
    """
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary='place_amenity',
                                       back_populates='amenities')
    else:
        name = ""
