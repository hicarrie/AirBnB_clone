#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel

'''test module for Console module'''


class TestConsole(unittest.TestCase):

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
