import unittest
import sys

sys.path.append("sources")
import Interface

class TestInterface(unittest.TestCase):
    def test_ShowMessage(self):
        Interface.ShowMessage("Test", "Test")

    def test_ShowFileDialog(self):
        Interface.ShowFileDialog()

