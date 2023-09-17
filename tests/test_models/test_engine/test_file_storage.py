import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage and save it in the storage module
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the test file, if it exists
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_new(self):
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        # Create an instance of a model and save it
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        # Create a new FileStorage instance to reload the data
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded data is correct
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, new_storage.all())

    def test_all(self):
        # Create instances of multiple models
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        # Add them to the storage
        self.storage.new(model1)
        self.storage.new(model2)
        self.storage.new(model3)

        # Check if all() returns a dictionary with the correct keys
        all_objects = self.storage.all()
        key1 = "{}.{}".format(model1.__class__.__name__, model1.id)
        key2 = "{}.{}".format(model2.__class__.__name__, model2.id)
        key3 = "{}.{}".format(model3.__class__.__name__, model3.id)
        self.assertIn(key1, all_objects)
        self.assertIn(key2, all_objects)
        self.assertIn(key3, all_objects)


if __name__ == '__main__':
    unittest.main()
