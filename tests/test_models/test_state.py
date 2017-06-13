#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.state import State
'''test module for State class'''


class TestAmenity(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of State/json file'''
        self.state = State()

    def tearDown(self):
        '''method to tear down instance of State/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.state)

    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.state.name, "")
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertFalse(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "id"))
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_to_json(self):
        '''method to check that the to_json function returns'''
        example_tojson = State.to_json(self.state)
        self.assertEqual(type(example_tojson), dict)

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.state), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.state.__str__())

if __name__ == "__main__":
    main()
