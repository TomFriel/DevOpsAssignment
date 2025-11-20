
# ---- tests ----
import unittest
from main import GameFeature

class TestGameFeature(unittest.TestCase):
    def test_basic_name(self):
        g = GameFeature()
        self.assertEqual(g.compute_score("alice"), 50)  # 5*10

    def test_spaces_and_empty(self):
        g = GameFeature()
        self.assertEqual(g.compute_score("  bob  "), 30)  # 3*10
        self.assertEqual(g.compute_score("   "), 0)
        
    # Refining test cases
    def test_whitespace(self):
        g = GameFeature()
        self.assertEqual(g.compute_score("\n\tjohn\t\n"), 40)  # 4*10

    def test_name_boundaries(self):
        g = GameFeature()
        name = "a" * 1000
        self.assertEqual(g.compute_score(name), 10000)  # 1000*10

    def test_non_string_input(self):
        g = GameFeature()
        with self.assertRaises(TypeError):
            g.compute_score(None)  # Non-string input    
               

if __name__ == "__main__":
    unittest.main()
