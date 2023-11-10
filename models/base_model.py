#!/usr/bin/python3

"""This module is the base model"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes"""

        # instance created from a dictionary, passed to the class
        if len(kwargs) > 0:
            for k in kwargs.keys():

                if k == "__class__":
                    continue

                elif k == "created_at" or k == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    kwargs[k] = datetime.strptime(kwargs[k], date_format)

                setattr(self, k, kwargs[k])

        # Instance created with no arguments passed to the class
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    # ___________________________________________________________________________________

    def __str__(self):
        """Returns the String representation of an instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    # ___________________________________________________________________________________

    def save(self):
        """Updates the attribute updated_at with the current datetime"""

        # Save the serialized __objects attribute to the json file
        models.storage.save()

        # Update the datetime when saving the object to the json file
        self.updated_at = datetime.now()

    # ___________________________________________________________________________________

    def to_dict(self):
        """Returns a dictionary contains __dict__ keys/values of instance"""

        instance_dict = self.__dict__.copy()

        instance_dict["__class__"] = self.__class__.__name__

        # Change datetime object to string format
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
