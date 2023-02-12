#!/usr/bin/python3
# test_file_storage.py
# Author: @tonybnya
"""
This is a test function for the File Storage Engine.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage class."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.fstorage = FileStorage()

    def tearDown(self):
        """Tear down test fixtures, if any."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Tests the all method returns an empty dictionary."""
        self.assertEqual(self.fstorage.all(), {})

    def test_new(self):
        """Tests the new method sets a new object in __objects."""
        model = BaseModel()
        model.id = "1"
        model.name = "Test"
        self.fstorage.new(model)
        self.assertEqual(len(self.fstorage.all()), 1)

    def test_save(self):
        """Tests the save method serializes __objects to the JSON file."""
        model = BaseModel()
        model.id = "1"
        model.name = "Test"
        self.fstorage.new(model)
        self.fstorage.save()
        with open("file.json") as file_obj:
            self.assertTrue("BaseModel.1" in json.load(file_obj))

    def test_reload(self):
        """Tests the reload method deserializes the JSON file to __objects."""
        model = BaseModel()
        model.id = "1"
        model.name = "Test"
        self.fstorage.new(model)
        self.fstorage.save()
        self.fstorage.reload()
        self.assertEqual(len(self.fstorage.all()), 1)


if __name__ == '__main__':
    unittest.main()
