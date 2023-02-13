#!/usr/bin/python3
# test_user.py
# Author: @tonybnya
"""
Unit tests for the User class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test class for the User model.
    """

    def setUp(self):
        """
        Set up the User instance for testing.
        """
        self.user = User()

    def test_class_exists(self):
        """
        Test if class exists.
        """
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """
        Test if the User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_user_type_email(self):
        """
        Test type of 'email' attribute.
        """
        self.assertIsInstance(self.user.email, str)

    def test_user_type_password(self):
        """
        Test type of 'password' attribute.
        """
        self.assertIsInstance(self.user.password, str)

    def test_user_type_first_name(self):
        """
        Test type of 'first_name' attribute.
        """
        self.assertIsInstance(self.user.first_name, str)

    def test_user_type_last_name(self):
        """
        Test type of 'last_name' attribute.
        """
        self.assertIsInstance(self.user.last_name, str)

    def test_user_type_id(self):
        """
        Test type of 'id' attribute.
        """
        self.assertIsInstance(self.user.id, str)

    def test_user_type_created_at(self):
        """
        Test type of 'created_at' attribute.
        """
        self.assertIsInstance(self.user.created_at, datetime)

    def test_user_type_updated_at(self):
        """
        Test type of 'updated_at' attribute.
        """
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_has_ttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
