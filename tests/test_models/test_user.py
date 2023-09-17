import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):

    def test_attributes_initialization(self):
        user = User()

        # Check that the attributes are initially empty strings
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict_method(self):
        user = User()
        user.email = "example@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_dict = user.to_dict()

        # Check that the to_dict method returns a dictionary with the expected keys and values
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'example@example.com')
        self.assertEqual(user_dict['password'], 'password123')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

        # Check that the 'created_at' and 'updated_at' keys are present and are in ISO format
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue(isinstance(user_dict['created_at'], str))
        self.assertTrue(isinstance(user_dict['updated_at'], str))

        # Check that 'created_at' and 'updated_at' strings can be converted to datetime objects
        created_at = datetime.fromisoformat(user_dict['created_at'])
        updated_at = datetime.fromisoformat(user_dict['updated_at'])

        self.assertTrue(isinstance(created_at, datetime))
        self.assertTrue(isinstance(updated_at, datetime))

    def test_str_representation(self):
        user = User()

        # Check that the __str__ method returns the expected string representation
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)


if __name__ == '__main__':
    unittest.main()
