import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def test_place_attributes(self):
        place = Place()

        # Check if the attributes have the correct initial values
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_inheritance(self):
        place = Place()

        # Check if Place inherits from BaseModel
        self.assertTrue(isinstance(place, Place))
        self.assertTrue(isinstance(place, BaseModel))


if __name__ == '__main__':
    unittest.main()
