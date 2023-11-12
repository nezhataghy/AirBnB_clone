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
    __classes = {"BaseModel": BaseModel}

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
        # objects_key = str(obj.__class__.__name__) + "." + str(obj.id)

        # Set the instance to the key has been created (`objects_key`)
        FileStorage.__objects[objects_key] = obj

    # _____________________________________________________________________________________

    def save(self):
        """Serializes __objects to the JSON file at __file_path"""

        # Convert the `__objects` values (obj) to a dictionary representation
        for k, v in FileStorage.__objects.items():
            FileStorage.__objects[k] = v.to_dict()

        # Convert the dictionary representation to a json string representation
        with open(FileStorage.__file_path, "w", encoding="utf8") as wf:
            json.dump(FileStorage.__objects, wf)

    # _____________________________________________________________________________________

    def reload(self):
        """
        deserializes the JSON file to __objects,
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        """

        # Do nothing, if the file does not exist
        if not exists(FileStorage.__file_path):
            return

        # convert the json string representation to dictionary representation
        with open(FileStorage.__file_path, 'r', encoding="utf8") as rf:
            loaded_data = json.load(rf)

        # Create instance from the extracted dictionary representation
        for k, obj_dict in loaded_data.items():
            class_name = obj_dict.get("__class__")

            # Convert the values of the dictionary (obj_dict) to instances
            if class_name in FileStorage.__classes:
                current_class = FileStorage.__classes[class_name]
                instance = current_class(**obj_dict)
                FileStorage.__objects[k] = instance
