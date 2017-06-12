#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
'''test module for __init__ class'''


class Test__init__(unittest.TestCase):

    def tearDown(self):
        '''method to tear down instance of BaseModel/json file'''
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test_init(self):
        '''method to check that initializing works'''
        before__init = storage.all()
        self.assertEqual(before__init, {})
        after__init = BaseModel()
        self.assertIsNotNone(after__init)
        self.assertTrue(type(after__init), dict)
