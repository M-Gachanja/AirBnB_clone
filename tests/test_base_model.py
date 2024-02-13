#!/usr/bin/python3
"""
Defines unittests for base_models.py
Classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import models
import unittest
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModelInstantiation(unnittest.TestCase):
    """Tests BaseModel class instantiation"""

    def test_no_args_instatiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_string_representation(self):
        dt = datetime.today()
        dr_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.update_at = dt
        bm_str = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bm_str)
        self.assertIn("'id': '123456'", bm_str)
        self.assertIn("'created_at: " + dt_repr, bm_str)
        self.assertIn("'updated_at: " + dt_repr, bm_str)

if __name__ == "__main__":
    unittest.main()
