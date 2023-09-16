import unittest
import os
import tempfile
import shutil
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        # Set the file path for testing
        self.test_file_path = os.path.join(self.test_dir, "test_storage.json")
        FileStorage._FileStorage__file_path = self.test_file_path

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_new_and_all(self):
        storage = FileStorage()
        data = {'__class__': 'TestObject', 'id': '1', 'name': 'Test'}
        storage.new(data)
        self.assertEqual(storage.all(), {"TestObject.1": data})

    def test_save_and_reload(self):
        storage = FileStorage()
        data = {'__class__': 'TestObject', 'id': '1', 'name': 'Test'}
        storage.new(data)
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(new_storage.all(), {"TestObject.1": data})

    def test_save_and_reload_nonexistent_file(self):
        storage = FileStorage()
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(new_storage.all(), {})


if __name__ == '__main__':
    unittest.main()
