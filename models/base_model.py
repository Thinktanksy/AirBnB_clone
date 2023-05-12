#!/usr/bin/python3
"""Defines the BaseModel classes"""

import models
from uuid import uuid
from datetime import datetime

class BaseModel():
    """defs all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
            Innitializes the instances attributes
            Args:
                *args - list of arguments
                **kwargs -  dict of key/value pairs of attributes
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(b, form)
                else:
                    self.__dict__[a] = b
        else:
            models.storage.new(self)

    def __str__(self):
        """Prints the official string representation of BaseModel"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of
            __dict__ of the instance
        """
        retdict = self.__dict__.copy
        retdict["created_at"] = self.created_at.isoformat()
        retdict["updated_at"] = self.updated_at.isoformat()
        retdict["__class__"] = self.__class__.__name__
        return retdict
