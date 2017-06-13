#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.review import Review

'''test module for Review class'''


class TestReview(unittest.TestCase):

    def setUp(self):
        '''method to set up instance of review/json file'''
        self.review = Review()

    def tearDown(self):
        '''method to tear down instance of review/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        '''method to check if instance initializes'''
        self.assertIsNotNone(self.review)

    def test_attributes(self):
        '''method to test if updates take place in save'''
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertFalse(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "id"))
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_to_json(self):
        '''method to check that the to_json function returns'''
        example_tojson = Review.to_json(self.review)
        self.assertEqual(type(example_tojson), dict)

    def test___str__(self):
        '''method to check that dict printing instance'''
        example = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        self.assertEqual(print(self.review), print(example))

    def test__repr__(self):
        '''method to print attributes of dictionary'''
        self.assertIsNotNone(self.review.__str__())

if __name__ == "__main__":
    main()
