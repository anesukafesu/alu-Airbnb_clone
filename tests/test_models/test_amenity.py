#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_amenity_attributes(self):
        amenity = Amenity()

        # Check if the 'name' attribute is initially an empty string
        self.assertEqual(amenity.name, "")

    def test_amenity_inheritance(self):
        amenity = Amenity()

        # Check if Amenity inherits from BaseModel
        self.assertTrue(isinstance(amenity, Amenity))
        self.assertTrue(isinstance(amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
