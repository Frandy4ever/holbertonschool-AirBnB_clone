#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertEqual(user.name, "")

    def test_state_save(self):
        state = State()
        initial_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(initial_updated_at, state.updated_at)

if __name__ == '__main__':
    unittest.main()
