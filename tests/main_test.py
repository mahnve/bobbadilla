import unittest
import data_builder
from nose.tools import assert_equal

sys.path.append(os.path.abspath(".."))

from bobbadilla import main


class BobbadillaTest(unittest.TestCase):
    def test_empty_m3u(self):
        m3u = data_builder.m3uBuilder().build()
        output = data_builder.

        the_file = file_reader.FileReader().read('build/test_data/1_mb_file')
        assert_equal(the_file['size'], 1)

    def test_size_of_non_existing_file_returns_None(self):
        the_file = file_reader.FileReader().read('build/test_data/non_existing')
        assert_equal(the_file, None)
