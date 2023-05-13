#!/usr/bin/python3
"""Module that creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for review objects"""

    place_id = ""
    user_id = ""
    text = ""
