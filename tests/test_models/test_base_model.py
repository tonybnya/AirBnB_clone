#!/usr/bin/python3
# test_base_model.py
# Author: @tonybnya
"""
This is a test function for the base class model.
"""
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for all the tests."""
        self.model = BaseModel()

    def test_init(self):
        """Tests the initialization of a new instance of BaseModel."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Tests the initialization of a new instance
        of BaseModel with kwargs.
        """
        dtime = datetime.today()
        model = BaseModel(created_at=dtime.isoformat(), random_attr="value")
        self.assertEqual(model.created_at, dtime)
        self.assertEqual(model.random_attr, "value")

    def test_str(self):
        """Tests the str method of BaseModel."""
        expected = "[BaseModel] ({}) {{'created_at': {}, 'id': '{}', \
            'updated_at': {}}}".format(
            self.model.id,
            self.model.created_at.isoformat(),
            self.model.id,
            self.model.updated_at.isoformat(),
        )
        self.assertEqual(str(self.model), expected)

    def test_save(self):
        """Tests the save method of BaseModel."""
        model_created_at = self.model.created_at
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)
        self.assertEqual(self.model.created_at, model_created_at)

    def test_to_dict(self):
        """Tests the to_dict method of BaseModel."""
        model_dict = self.model.to_dict()
        expected_keys = ["created_at", "id", "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), expected_keys)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
