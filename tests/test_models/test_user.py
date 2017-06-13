#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.user import User

'''test module for User class'''


class TestUser(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of BaseModel/json file'''
        self.user = User()

    def tearDown(self):
        '''method to tear down instance of BaseModel/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.user)

    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertFalse(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "id"))
        self.user.save()
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_to_json(self):
        '''method to check that the to_json function returns'''
        example_tojson = User.to_json(self.user)
        self.assertEqual(type(example_tojson), dict)

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.user), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.user.__str__())

if __name__ == "__main__":
    main()
