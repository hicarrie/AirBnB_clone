#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    '''test module for BaseModel class'''

    def setUp(self):
        '''method to set up instance of BaseModel/json file'''
        new_inst = BaseModel()

    def tearDown(self):
        '''method to tear down instance of BaseModel/json file'''
        if os.path.exist("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_save_init(self):
        '''method to check if initial save is accurate'''
        assertIsNotNone(new_inst.__objects.get["updated_at"])

    def test_save_update(self):
        '''method to test if updates take place in save'''
        before = new_inst.__objects.get["updated_at"]
        new_inst.save()
        after = new_inst.__objects.get["updated_at"]
