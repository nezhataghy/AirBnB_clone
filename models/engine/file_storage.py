#!/usr/bin/python3
"""This module is the storage engine of the objects"""

import json
from models.base_model import BaseModel
from os.path import exists


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    # __classes = {"BaseModel": BaseModel}

    def all(self):
        """Returns the dictionary `__objects` while values are instances"""

        return FileStorage.__objects

    # _____________________________________________________________________________________

    def new(self, obj):
        """
         Sets in `__objects` the `obj` with key <obj class name>.id

         args:
            obj: The instance of the class
        """

        # Create string format for the key of `__objects` attribute
        objects_key = f"{obj.__class__.__name__}.{obj.id}"

        # Set the instance to the key has been created (`objects_key`)
        FileStorage.__objects[objects_key] = obj

    # _____________________________________________________________________________________

    def save(self):
        """Serializes __objects to the JSON file at __file_path"""

        dict_of_obj = {}
        # Convert the `__objects` values (obj) to a dictionary representation
        for k, v in FileStorage.__objects.items():
            dict_of_obj[k] = v.to_dict()

        # Convert the dictionary representation to a json string representation
        with open(FileStorage.__file_path, "w", encoding="utf8") as wf:
            json.dump(dict_of_obj, wf)

    # _____________________________________________________________________________________

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                dictionary = json.loads(file.read())
                for value in dictionary.values():
                    cls_name = value["__class__"]
                    self.new(eval(cls_name)(**value))
        except Exception:
            pass
