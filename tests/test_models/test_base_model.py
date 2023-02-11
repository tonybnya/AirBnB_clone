#!/usr/bin/python3
# test_base_model.py
# Author: @tonybnya
"""
This is a test function for the base class model.
"""
import unittest
from datetime import datetime
from AirBnB_clone.models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for all the tests."""
        self.base_model = BaseModel()

    def test_init(self):
        """Test the initialization of an instance."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of an instance."""
        self.assertIsInstance(str(self.base_model), str)

    def test_save(self):
        """Test the save method updating the 'updated_at' attribute."""
        updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method returning a dict representation."""
        self.assertIsInstance(self.base_model.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
