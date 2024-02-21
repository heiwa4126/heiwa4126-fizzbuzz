import unittest
from heiwa4126_fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        result = list(fizzbuzz(15))
        self.assertEqual(
            result,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )

    def test_fizzbuzz_custom_range(self):
        result = list(fizzbuzz(20))
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
            "16",
            "17",
            "Fizz",
            "19",
            "Buzz",
        ]
        self.assertEqual(result, expected)

    def test_fizzbuzz_empty_range(self):
        result = list(fizzbuzz(0))
        self.assertEqual(result, [])

    def test_fizzbuzz_negative_range(self):
        result = list(fizzbuzz(-10))
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
