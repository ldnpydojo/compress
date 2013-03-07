from unittest.case import TestCase
from uncompress import uncompress


class UncompressTest(TestCase):

    def test_valid(self):
        compressed = "abc|foo|bar\n$1 $2 xxx $0 $0 $0 $2 $1 $0 $0 $0"
        self.assertEqual("foo bar xxx abc abc abc bar foo abc abc abc", uncompress(compressed))

    def test_harder(self):
        compressed = "abc|foo|bar\n$1 $2 xxx $0 $0 $0 $2 $1 $0 $0 $4 $"
        self.assertEqual("foo bar xxx abc abc abc bar foo abc abc $4 $", uncompress(compressed))