import unittest

from src.load import get_max_id


class TestPipeline(unittest.TestCase):

    def test_get_max_id(self):
        max_id = get_max_id()

        self.assertIsNotNone(max_id) #Expects to get an ID, not None


if __name__ == "__main__":
    unittest.main()