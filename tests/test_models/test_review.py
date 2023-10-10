#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_save(self):
        review = Review()
        initial_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(initial_updated_at, review.updated_at)

if __name__ == '__main__':
    unittest.main()
