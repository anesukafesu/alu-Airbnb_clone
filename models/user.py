#!/usr/bin/python3
"""Module for the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class
    attributes: email, password, first_name, last_name
    """
    email, password, first_name, last_name = "", "", "", ""
