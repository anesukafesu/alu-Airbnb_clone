import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def test_city_attributes(self):
        city = City()

        # Check if the 'state_id' and 'name' attributes are initially empty strings
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_inheritance(self):
        city = City()

        # Check if City inherits from BaseModel
        self.assertTrue(isinstance(city, City))
        self.assertTrue(isinstance(city, BaseModel))


if __name__ == '__main__':
    unittest.main()
