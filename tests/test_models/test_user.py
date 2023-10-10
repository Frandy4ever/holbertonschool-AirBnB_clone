#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_save(self):
        user = User()
        initial_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(initial_updated_at, user.updated_at)

if __name__ == '__main__':
    unittest.main()
