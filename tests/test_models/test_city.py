#!/usr/bin/python3
"""Tests City class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City Class"""

    def setUp(self):
        """Initializes on each test method"""
        self.c1 = City()
        self.c1.state_id = "21412"
        self.c1.name = "Alexandria"

    def test_instance_init(self):
        """tests that the City class Inherits from BaseModel"""
        self.assertIsInstance(self.c1, BaseModel)
        self.assertIsInstance(self.c1.state_id, str)
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1, City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_review_attrs(self):
        """tests that the City attributes are present"""
        self.assertIn("state_id", self.c1.__dict__)
        self.assertIn("name", self.c1.__dict__)

    def test_empty_att(self):
        """Test if attrs is None"""
        self.city = City()
        self.city.name = None

        self.assertIsNone(self.city.name)
