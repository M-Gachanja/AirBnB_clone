#!/usr/bin/python3
"""
Defines unittests for base_models.py
Classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import unittest
from models.base_model import BaseModel

class TestBaseModelInstantiation(unittest.TestCase):
    """Tests BaseModel class instantiation"""

    def test_string_representation(self):
        """
        Test the string representation of BaseModel.
        """
        bm = BaseModel()
        bm.name = "My_First_Model"
        bm.my_number = 89
        self.assertIn("[BaseModel] ({})".format(bm.id), str(bm))

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        """
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        bm = BaseModel()
        bm.name = "My_First_Model"
        bm.my_number = 89
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertIn("__class__", bm_dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("id", bm_dict)
        self.assertIn("name", bm_dict)
        self.assertIn("my_number", bm_dict)


if __name__ == "__main__":
    unittest.main()
