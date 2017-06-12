#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel

'''test module for BaseModel class'''


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of BaseModel/json file'''
        self.basemodel = BaseModel()

    def tearDown(self):
        '''method to tear down instance of BaseModel/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.basemodel)

    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertFalse(hasattr(self.basemodel, "updated_at"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def test_to_json(self):
        '''method to check that the to_json function returns'''
        example_tojson = BaseModel.to_json(self.basemodel)
        self.assertEqual(type(example_tojson), dict)

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.basemodel), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.basemodel.__str__())

if __name__ == "__main__":
    main()
