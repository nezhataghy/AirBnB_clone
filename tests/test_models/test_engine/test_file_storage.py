#!/usr/bin/python3
"""Test module for file_storage"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class test_file_storage(unittest.TestCase):
  """defines test cases for the file_storage"""

  def setUp(self):
    """Initializes on each test method"""

    self.b_model = BaseModel()
    self.storage = FileStorage()

  # _____________________________________________________________________________________

  def test_pv_attrs(self):
    """Check the private attributes if it is private."""
    
    
    with self.assertRaises(AttributeError):
      self.assertEqual(FileStorage.__file_path, "file.json")
      self.assertEqual(self.storage.__file_path, "file.json")
      self.assertEqual(self.storage._file_path, "file.json")
      self.assertEqual(self.storage.file_path, "file.json")
      self.assertEqual(FileStorage.__objects, "file.json")
      self.assertEqual(self.storage.__objects, "file.json")
      self.assertEqual(self.storage._object, "file.json")
      self.assertEqual(self.storage.object, "file.json")

  # _____________________________________________________________________________________

  def test_object_type(self):
    """Test __objects if it is empty"""
    
    all_objects = self.storage.all()

    self.assertIs(type(all_objects), dict)

    for v in all_objects.values():
      self.assertNotIsInstance(v, dict)
  
  # _____________________________________________________________________________________

  def test_new_with_noArg(self):

    with self.assertRaises(TypeError):
      self.storage.new()

  # _____________________________________________________________________________________

  def test_new_with_moreArgs(self):

    with self.assertRaises(TypeError):
      self.storage.new("ehab", "aysha")

  # _____________________________________________________________________________________

  def test_object_notempty(self):
    """Call new and check if __objects is not empty"""

    # self.storage.new(self.b_model)
    # self.storage._FileStorage__file_path
    # key_format = f"{self.b_model.__class__.__name__}.{self.b_model.id}"

    
