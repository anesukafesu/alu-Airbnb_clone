import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage
        self.storage = FileStorage()

    def tearDown(self):
        # Delete the test file if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new_and_all(self):
        # Create a BaseModel instance and add it to FileStorage
        obj = BaseModel()
        self.storage.new(obj)

        # Check if the object was added to the __objects dictionary
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_save_and_reload(self):
        # Create a BaseModel instance and add it to FileStorage
        obj = BaseModel()
        self.storage.new(obj)

        # Save the objects to a file
        self.storage.save()

        # Create a new instance of FileStorage
        new_storage = FileStorage()

        # Reload objects from the file
        new_storage.reload()

        # Check if the reloaded object exists in the new storage
        self.assertIn("BaseModel.{}".format(obj.id), new_storage.all())

    def test_save_file_creation(self):
        # Check if the save() method creates a file
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()
