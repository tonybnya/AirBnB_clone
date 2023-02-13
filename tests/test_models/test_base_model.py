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
# from uuid import uuid4
# from models import storage

# class TestBaseModel(unittest.TestCase):
#     """Test cases for the BaseModel class."""

#     def setUp(self):
#         """Set up a BaseModel instance for all the tests."""
#         self.model = BaseModel()

#     def test_init(self):
#         """Test the initialization of an instance."""
#         self.assertIsInstance(self.model, BaseModel)
#         self.assertIsInstance(self.model.id, str)
#         self.assertIsInstance(self.model.created_at, datetime)
#         self.assertIsInstance(self.model.updated_at, datetime)

#     def test_id_is_a_uuid(self):
#         """Test if the 'id' attribute is a UUID."""
#         self.assertIsInstance(uuid4(hex=self.model.id), uuid4)

#     def test_created_and_updated_at_are_equal(self):
#         """Test if the 'created_at' and 'updated_at' are equal."""
#         self.assertEqual(self.model.created_at, self.model.updated_at)

#     def test_str(self):
#         """Test the string representation of an instance."""
#         self.assertIsInstance(str(self.model), str)

#     def test_save(self):
#         """Test the save method updating the 'updated_at' attribute."""
#         updated_at = self.model.updated_at
#         self.model.save()
#         self.assertNotEqual(updated_at, self.model.updated_at)

#     def test_to_dict(self):
#         """Test the to_dict returns a dict representation."""
#         self.assertIsInstance(self.model.to_dict(), dict)

#     def test_to_dict_created_at_is_str(self):
#         """Test if the 'created_at' value in the dictionary
#         returned by 'to_dict' is a string.
#         """
#         self.assertIsInstance(self.model.to_dict()["created_at"], str)

#     def test_to_dict_updated_at_is_str(self):
#         """Test if the 'updated_at' value in the dictionary
#         returned by 'to_dict' is a string.
#         """
#         self.assertIsInstance(self.model.to_dict()["updated_at"], str)

#     def test_to_dict_class_key_exists(self):
#         """Test if the '__class__' key exists in the dictionary
#         returned by 'to_dict'.
#         """
#         self.assertIn("__class__", self.model.to_dict())

#     def test_to_dict_class_value_is_str(self):
#         """Test if the value of the '__class__' key in the dictionary
#         returned by 'to_dict' is a string.
#         """
#         self.assertIsInstance(self.model.to_dict()["__class__"], str)


class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class."""

    def test_init(self):
        """Tests the initialization of a new instance of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

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
        model = BaseModel()
        expected = "[BaseModel] ({}) {{'created_at': {}, 'id': '{}', \
            'updated_at': {}}}".format(
            model.id,
            model.created_at.isoformat(),
            model.id,
            model.updated_at.isoformat(),
        )
        self.assertEqual(str(model), expected)

    def test_save(self):
        """Tests the save method of BaseModel."""
        model = BaseModel()
        model_created_at = model.created_at
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertEqual(model.created_at, model_created_at)

    def test_to_dict(self):
        """Tests the to_dict method of BaseModel."""
        model = BaseModel()
        model_dict = model.to_dict()
        expected_keys = ["created_at", "id", "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), expected_keys)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"],
                         model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
