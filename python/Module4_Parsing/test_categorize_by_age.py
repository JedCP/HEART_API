import unittest
def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden Age"
    else:
        return f"Invalid Age: {age}"
class TestCategorizeByAge(unittest.TestCase):
    def test_Child(self):
        self.assertEqual(categorize_by_age(10), "Child")
    def test_Adolescent(self):
        self.assertEqual(categorize_by_age(19), "Adolescent")
    def test_Adult(self):
        self.assertEqual(categorize_by_age(66), "Adult")
    def test_Golden_age(self):
        self.assertEqual(categorize_by_age(151), "Golden Age")
    def test_Negative_age(self):
        self.assertEqual(categorize_by_age(-2), "Invalid Age: -1")
    def test_Too_old(self):
        self.assertEqual(categorize_by_age(151), "Invalid Age: 151")
if __name__ == '__main__':
    unittest.main() 