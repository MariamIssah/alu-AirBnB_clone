 BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Defines common attributes and methods for other classes.
    
    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp when an instance is created.
        updated_at (datetime): Timestamp updated whenever an instance is modified.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
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
        """Update `updated_at` with the current datetime and save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance, including class name."""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
