#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.city import City

'''test module for City class'''


class TestCity(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of city/json file'''
        self.city = City()

    def tearDown(self):
        '''method to tear down instance of city/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.city)

    def test_attributes(self):
        '''method to test if updates take place in save'''
        name = ""
        state_id = ""
        self.assertEqual(self.city.name, "")
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertFalse(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "id"))
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_to_json(self):
        '''method to check that the to_json function returns'''
        example_tojson = City.to_json(self.city)
        self.assertEqual(type(example_tojson), dict)

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.city), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.city.__str__())

if __name__ == "__main__":
    main()
