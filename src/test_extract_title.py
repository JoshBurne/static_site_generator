import unittest
from extract_title import extract_title


class Test_Extract_title_from_markdown(unittest.TestCase):
    def test_title_exctraction(self):
        md = "# This is the heading. \nThis is the paragraph"
        function = extract_title(md)
        expected = "This is the heading."
        self.assertEqual(function, expected)




if __name__ == "__main__":
    unittest.main()