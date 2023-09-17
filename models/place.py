#!/usr/bin/python3
"""Module for the Place model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Model for Place
    attributes: city_id, user_id, name, description,
    number_rooms, number_bathrooms, max_guest,
    price_by_night, latitude, longitude, amenity_ids
    """
    city_id, user_id, name, description = "", "", "", ""
    number_rooms, number_bathrooms, max_guest, price_by_night = 0, 0, 0, 0
    latitude, longitude = 0.0, 0.0
    amenity_ids = []
