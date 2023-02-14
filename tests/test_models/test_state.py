#!/usr/bin/python3
# test_state.py
# Author: @tonybnya
"""
Unittest for state.py
"""
import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Tests instances and methods from State class """

    def setUp(self):
        """Set up a State instance for all the tests."""
        self.state = State()

    def test_class_exists(self):
        """tests if class exists"""
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state)), result)

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, State)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
