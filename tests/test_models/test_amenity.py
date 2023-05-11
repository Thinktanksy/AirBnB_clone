#!/usr/bin/env python3
"""Unit testing module for Amenity Class"""

import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity
import time
import re
import json
import uuid
import datetime
from models import storage
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    """Test case for the Amenity model class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    # def test_has_attributes(self):
    #    self.assertTrue('id' in self.amenity.__dict__)
    #    self.assertTrue('created_at' in self.amenity.__dict__)
    #    self.assertTrue('updated_at' in self.amenity.__dict__)
    #    self.assertTrue('name' in self.amenity.__dict__)
    # OR
    a = Amenity()
    def test_has_attributes(self):
        """verify existence of the attributes"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_attributes_are_string(self):
        self.assertIs(type(self.amenity.name), str)

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self):
        """test if Amenity is subclass of a BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_types(self):
        """Verify if the attribute's type is correct using a test case"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
