#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.place import Place

'''test module for Place class'''


class TestAmenity(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of Place/json file'''
        self.place = Place()

    def tearDown(self):
        '''method to tear down instance of Place/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.place)

    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, "")
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertFalse(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "id"))
        self.place.save()
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_to_json(self):
        '''method to check that the to_json function returns'''
        example_tojson = Place.to_json(self.place)
        self.assertEqual(type(example_tojson), dict)

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.place), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.place.__str__())

if __name__ == "__main__":
    main()
