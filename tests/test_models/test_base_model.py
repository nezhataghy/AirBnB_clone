#!/usr/bin/python3
"""Unittest for the BaseModel"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class test_base_model(unittest.TestCase):
    """defines test cases for the base model"""

    def setUp(self):
        """Initializes on each test method"""
        self.b1 = BaseModel()

    def tearDown(self):
        """Initilaizes after each test method"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # _________________________________________________________

    def test_id_type(self):
        """Tests the instance id type"""

        self.assertIs(type(self.b1.id), str)

    # _________________________________________________________

    def test_str_method(self):
        """Tests the string representation of an instance"""

        str_format = (f"[{self.b1.__class__.__name__}] ({self.b1.id})"
                      f" {self.b1.__dict__}")

        self.assertEqual(str(self.b1), str_format)

    # _________________________________________________________

    def test_instance_update(self):
        """Tests the id updation"""

        b1_current_datetime = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(b1_current_datetime, self.b1.updated_at)

    # _________________________________________________________

    def test_class_property(self):
        """Tests if the __class__ property exists"""

        b1_json = self.b1.to_dict()
        self.assertIn("__class__", b1_json)

    # _________________________________________________________

    def test_creationUpdation_type(self):
        """Tests the type of created_at and updated_at attributes"""

        b1_json = self.b1.to_dict()
        self.assertIsInstance(b1_json["created_at"], str)
        self.assertIsInstance(b1_json["updated_at"], str)

    # _________________________________________________________

    def test_instantiation(self):
        """Tests instantiation of the class"""

        self.assertIsInstance(self.b1, BaseModel)

    # _________________________________________________________

    def test_empty_kwargs(self):
        """Tests the attributes when no kwargs"""

        my_attributes = ("id", "created_at", "updated_at")

        for att in my_attributes:
            self.assertIn(att, self.b1.__dict__)

    # _________________________________________________________

    def test_not_empty_kwargs(self):
        """Tests the attributes when there's kwargs"""

        self.b1.name = "My_First_Model"
        self.b1.my_number = 89
        b1_json = self.b1.to_dict()

        b2 = BaseModel(**b1_json)

        # Check __class__ is not exist in instance's attributes
        self.assertNotIn("__class__", b2.__dict__)

        # Check the type of created_at & updated_at
        self.assertIsInstance(b2.created_at, datetime)
        self.assertIsInstance(b2.updated_at, datetime)
