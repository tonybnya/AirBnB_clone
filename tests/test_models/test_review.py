#!/usr/bin/python3
# test_review.py
# Author: @tonybnya
"""
Unittest for review.py
"""
import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests instances and methods from Review class"""

    def setUp(self):
        """Set up a Review instance for all the tests."""
        self.review = Review()

    def test_class_exists(self):
        """tests if class exists"""
        result = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.review)), result)

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review, Review)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
