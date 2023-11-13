#!/usr/bin/python3
"""Tests User class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):

    def setUp(self):
        """Initializes on each test method"""
        self.a1 = Amenity()
        self.a1.name = "jacozy"

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_init(self):
        """tests that the Amenity class Inherits from BaseModel"""
        self.assertIsInstance(self.a1, BaseModel)
        self.assertIsInstance(self.a1, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.a1.name, str)

    def test_review_attrs(self):
        """tests that the Amenity attributes are present"""
        self.assertIn("name", self.a1.__dict__)

    def test_empty_att(self):
        """Test if attrs is None"""
        self.amenity = Amenity()
        self.amenity.name = None

        self.assertIsNone(self.amenity.name)
