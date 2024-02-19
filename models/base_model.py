#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Defines all common attrs/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value, timeformat))
                    else:
                        setattr(self, key, value)
                else:
                    models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel class instance
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attr updated_at with current date/time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dict containing all key/values of __dict__ of instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
