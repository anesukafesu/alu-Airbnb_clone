# 1/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_review_attributes(self):
        review = Review()

        # Check if the attributes are initially empty strings
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_inheritance(self):
        review = Review()

        # Check if Review inherits from BaseModel
        self.assertTrue(isinstance(review, Review))
        self.assertTrue(isinstance(review, BaseModel))


if __name__ == '__main__':
    unittest.main()
