#!/usr/bin/python3
"""Tests User class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place


class TestUser(unittest.TestCase):

    def setUp(self):
        """Initializes on each test method"""
        self.p1 = Place()
        self.p1.city_id = "21412"
        self.p1.user_id = "75222"
        self.p1.name = "Pyramids"
        self.p1.description = "Excellent, It's good"
        self.p1.number_rooms = 6
        self.p1.number_bathrooms = 3
        self.p1.max_guest = 30
        self.p1.price_by_night = 180
        self.p1.latitude = 6.5
        self.p1.longitude = 6.5
        self.p1.amenity_ids = ['pool', 'football']


    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_init(self):
        """tests that the Place class Inherits from BaseModel"""
        self.assertIsInstance(self.p1, BaseModel)
        self.assertIsInstance(self.p1, Place)
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

    def test_review_attrs(self):
        """tests that the Review attributes are present"""
        self.assertIn("city_id", self.p1.__dict__)
        self.assertIn("user_id", self.p1.__dict__)
        self.assertIn("name", self.p1.__dict__)
        self.assertIn("description", self.p1.__dict__)
        self.assertIn("number_rooms", self.p1.__dict__)
        self.assertIn("number_bathrooms", self.p1.__dict__)
        self.assertIn("max_guest", self.p1.__dict__)
        self.assertIn("price_by_night", self.p1.__dict__)
        self.assertIn("latitude", self.p1.__dict__)
        self.assertIn("longitude", self.p1.__dict__)
        self.assertIn("amenity_ids", self.p1.__dict__)

    def test_empty_att(self):
        """Test if attrs is None"""
        self.review = Place()
        self.review.description = None

        self.assertIsNone(self.review.description)
