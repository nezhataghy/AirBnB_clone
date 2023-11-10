#!/usr/bin/python3

"""This module is the base model"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes"""

        if len(kwargs) > 0:
            for k in kwargs.keys():
                
                if k == "__class__":
                    continue

                elif k == "created_at" or k == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    kwargs[k] = datetime.strptime(kwargs[k], date_format)

                setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    # ___________________________________________________________________________

    def __str__(self):
        """Returns the String representation of an instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    # ___________________________________________________________________________

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        models.storage.save()
        self.updated_at = datetime.now()

    # ___________________________________________________________________________

    def to_dict(self):
        """Returns a dictionary contains __dict__ keys/values of instance"""

        instance_dict = self.__dict__.copy()

        instance_dict["__class__"] = self.__class__.__name__

        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
