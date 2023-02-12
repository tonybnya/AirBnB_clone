#!/usr/bin/python3
# test_base_model.py
# Author: @tonybnya
"""
This is a test function for the base class model.
"""
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for all the tests."""
        self.model = BaseModel()

    def test_init(self):
        """Test the initialization of an instance."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_id_is_a_uuid(self):
        """Test if the 'id' attribute is a UUID."""
        self.assertIsInstance(uuid4(hex=self.model.id), uuid4)

    def test_created_and_updated_at_are_equal(self):
        """Test if the 'created_at' and 'updated_at' are equal."""
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str(self):
        """Test the string representation of an instance."""
        self.assertIsInstance(str(self.model), str)

    def test_save(self):
        """Test the save method updating the 'updated_at' attribute."""
        updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict returns a dict representation."""
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_to_dict_created_at_is_str(self):
        """Test if the 'created_at' value in the dictionary
        returned by 'to_dict' is a string.
        """
        self.assertIsInstance(self.model.to_dict()["created_at"], str)

    def test_to_dict_updated_at_is_str(self):
        """Test if the 'updated_at' value in the dictionary
        returned by 'to_dict' is a string.
        """
        self.assertIsInstance(self.model.to_dict()["updated_at"], str)

    def test_to_dict_class_key_exists(self):
        """Test if the '__class__' key exists in the dictionary
        returned by 'to_dict'.
        """
        self.assertIn("__class__", self.model.to_dict())

    def test_to_dict_class_value_is_str(self):
        """Test if the value of the '__class__' key in the dictionary
        returned by 'to_dict' is a string.
        """
        self.assertIsInstance(self.model.to_dict()["__class__"], str)


if __name__ == '__main__':
    unittest.main()
