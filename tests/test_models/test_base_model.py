import unittest
from datetime import datetime
from your_module import BaseModel  # Replace 'your_module' with the actual module name

class TestBaseModel(unittest.TestCase):

    def test_init_defaults(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_args(self):
        model_data = {
            "id": "12345",
            "created_at": "2023-09-16T12:34:56",
            "updated_at": "2023-09-16T12:45:00",
            "custom_attribute": "custom_value"
        }
        model = BaseModel(**model_data)
        self.assertEqual(model.id, model_data["id"])
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.custom_attribute, "custom_value")

    def test_str(self):
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
