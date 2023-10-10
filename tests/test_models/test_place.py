#!/usr/bin/python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.place_id, "")
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

    def test_place_amenity_ids_type(self):
        place = Place()
        place.amenity_ids = "1,2,3"
        self.assertNotEqual(place.amenity_ids, ["1", "2", "3"])
        self.assertTrue(isinstance(place.amenity_ids, list))

if __name__ == '__main__':
    unittest.main()