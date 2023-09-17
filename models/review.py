#!/usr/bin/python3
"""Module for the Review model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Model for Review
    attributes: place_id, user_id, text
    """
    place_id, user_id, text = "", "", ""
