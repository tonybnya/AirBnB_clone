#!/usr/bin/python3
# test_amenity.py
# Author: @tonybnya
"""
Unittest for amenity.py
"""
import unittest
import datetime
import models
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    def setUp(self):
        """Set up a Amenity instance for all the tests."""
        self.amen = models.amenity.Amenity()

    def test_class_exists(self):
        """tests if class exists"""
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amen)), result)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amen, BaseModel)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.amen, 'name'))
        self.assertTrue(hasattr(self.amen, 'id'))
        self.assertTrue(hasattr(self.amen, 'created_at'))
        self.assertTrue(hasattr(self.amen, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.amen.name, str)
        self.assertIsInstance(self.amen.id, str)
        self.assertIsInstance(self.amen.created_at, datetime.datetime)
        self.assertIsInstance(self.amen.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
