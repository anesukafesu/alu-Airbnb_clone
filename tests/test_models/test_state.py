import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_state_attributes(self):
        state = State()

        # Check if the 'name' attribute is initially an empty string
        self.assertEqual(state.name, "")

    def test_state_inheritance(self):
        state = State()

        # Check if State inherits from BaseModel
        self.assertTrue(isinstance(state, State))
        self.assertTrue(isinstance(state, BaseModel))


if __name__ == '__main__':
    unittest.main()
