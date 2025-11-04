#Unit Test Example

class GameFeature:
    # Rule: score = 10 × length of the trimmed name
    def compute_score(self, username: str) -> int:
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        name = username.strip()
        return 0 if name == "" else len(name) * 10


# ---- tests ----
import unittest

class TestGameFeature(unittest.TestCase):
    def test_basic_name(self):
        g = GameFeature()
        self.assertEqual(g.compute_score("alice"), 50)  # 5*10

    def test_spaces_and_empty(self):
        g = GameFeature()
        self.assertEqual(g.compute_score("  bob  "), 30)  # 3*10
        self.assertEqual(g.compute_score("   "), 0)

if __name__ == "__main__":
    unittest.main()
