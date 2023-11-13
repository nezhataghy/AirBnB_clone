#!/usr/bin/python3
"""Tests Review class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review Class"""
    def setUp(self):
        """Initializes on each test method"""
        self.r1 = Review()
        self.r1.place_id = "21412"
        self.r1.user_id = "75222"
        self.r1.text = "Excellent, It's good"

    def tearDown(self):
        """Initilaizes after each test method"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_init(self):
        """tests that the Review class Inherits from BaseModel"""
        self.assertIsInstance(self.r1, BaseModel)
        self.assertIsInstance(self.r1, Review)
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

    def test_review_attrs(self):
        """tests that the Review attributes are present"""
        self.assertIn("place_id", self.r1.__dict__)
        self.assertIn("user_id", self.r1.__dict__)
        self.assertIn("text", self.r1.__dict__)
        self.assertEqual(self.r1.place_id, "21412")
        self.assertEqual(self.r1.user_id, "75222")
        self.assertEqual(self.r1.text, "Excellent, It's good")

    def test_empty_att(self):
        """Test if attrs is None"""
        self.review = Review()
        self.review.place_id = None
        self.review.user_id = None
        self.review.text = None

        self.assertIsNone(self.review.place_id)
        self.assertIsNone(self.review.user_id)
        self.assertIsNone(self.review.text)
