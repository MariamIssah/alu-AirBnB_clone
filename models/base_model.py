#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    
    Attributes:
        id (str): A unique id generated using uuid when an instance is created.
        created_at (datetime): The current datetime when an instance is created.
        updated_at (datetime): The current datetime when an instance is created and 
                               updated every time the object changes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], tform)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], tform)
            self.__dict__.update(kwargs)
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance, including class name."""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
