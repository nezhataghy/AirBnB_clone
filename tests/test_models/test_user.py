#!/usr/bin/python3
"""Tests User class"""

import os
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User Class"""

    def setUp(self):
        """Initializes on each test method"""
        self.u1 = User()

    def tearDown(self):
        """Initilaizes after each test method"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_init(self):
        """tests that the User class Inherits from BaseModel"""
        self.assertIsInstance(self.u1, BaseModel)
        self.assertIsInstance(self.u1, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attrs(self):
        """tests that the user attributes are present"""
        self.assertIn("email", self.u1.__dict__)
        self.assertIn("password", self.u1.__dict__)
        self.assertIn("first_name", self.u1.__dict__)
        self.assertIn("last_name", self.u1.__dict__)

    def test_user_attrs(self):
        """tests that the user attributes are present"""
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)

    def test_empty_att(self):
        """Test if attrs is None"""
        self.user = User()
        self.user.email = None
        self.user.password = None

        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.password)
