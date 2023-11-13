#!/usr/bin/python3
"""Tests User class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):

    def setUp(self):
        """Initializes on each test method"""
        self.s1 = State()
        self.s1.name = "NYC"

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_init(self):
        """tests that the State class Inherits from BaseModel"""
        self.assertIsInstance(self.s1, BaseModel)
        self.assertIsInstance(self.s1, State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attrs(self):
        """tests that the State attributes are present"""
        self.assertIn("name", self.s1.__dict__)
        self.assertEqual(self.s1.name, "NYC")

    def test_empty_att(self):
        """Test if attrs is None"""
        self.user = State()
        self.user.name = None

        self.assertIsNone(self.user.name)
