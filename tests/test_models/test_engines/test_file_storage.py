from models.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        # Ensure the __objects dictionary is initially empty
        self.assertEqual(self.storage.all(), {})

    def test_new_and_all(self):
        # Create a BaseModel instance
        model = BaseModel()
        # Add it to storage
        self.storage.new(model)
        # Ensure the model is in the __objects dictionary
        self.assertIn(f"BaseModel.{model.id}", self.storage.all())

    def test_save_and_reload(self):
        # Create a BaseModel instance
        model = BaseModel()
        # Add it to storage
        self.storage.new(model)
        # Save the data to a file
        self.storage.save()
        # Reload the data from the file
        new_storage = FileStorage()
        new_storage.reload()
        # Ensure the reloaded data contains the model
        self.assertIn(f"BaseModel.{model.id}", new_storage.all())

    def test_save_and_reload_nonexistent_file(self):
        # Attempt to reload data from a nonexistent file
        new_storage = FileStorage()
        new_storage.reload()
        # Ensure the result is an empty dictionary
        self.assertEqual(new_storage.all(), {})


if __name__ == '__main__':
    unittest.main()
