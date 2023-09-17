#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_json(self):
        base = BaseModel()
        base_json = base.to_dict()

        self.assertIsInstance(base_json, dict)

        self.assertIn("id", base_json)
        self.assertIn("created_at", base_json)
        self.assertIn("updated_at", base_json)
        self.assertIn("__class__", base_json)
        self.assertEqual(base.id, base_json["id"])
        self.assertEqual("BaseModel", base_json["__class__"])

    def test_kwarg(self):
        basemodel = BaseModel()
        self.assertEqual(basemodel.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == "__main__":
    unittest.main()
