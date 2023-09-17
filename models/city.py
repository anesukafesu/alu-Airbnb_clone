#!/usr/bin/python3
"""Module for the City model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City model
    attributes: state_id, name
    """
    state_id, name = "", ""
