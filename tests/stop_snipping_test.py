import unittest

from src.stop_snipping import spin_words


class StopSnippingTest(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words("to"), "to")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")

    def test_multi_word(self):
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")


if __name__ == "__main__":
    unittest.main()
