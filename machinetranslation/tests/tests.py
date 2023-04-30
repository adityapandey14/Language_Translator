import unittest
import os
import sys

sys.path.append(os.path.abspath("D:/Cprogram/machinetranslation"))
from translation import englishToFrench , frenchToEnglish

class Testfrench(unittest.TestCase):
  def test1(self):
    self.assertEqual(englishToFrench("Hello"),"Bonjour")
    self.assertIsNone(englishToFrench(None),None)
    

class Testenglish(unittest.TestCase):
  def test1(self):
    self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
    self.assertIsNone(frenchToEnglish(None), None)


if __name__ == '__main__':
    unittest.main()