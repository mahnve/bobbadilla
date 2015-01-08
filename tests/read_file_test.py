import unittest
import os
import sys
import data_builder

sys.path.append(os.path.abspath(".."))

from bobbadilla import file_reader


from nose.tools import assert_equal


class ReadFileTest(unittest.TestCase):
    def test_read_size_of_a_1_mb_file(self):
        data_builder.FileBuilder().with_path(
            'build/test_data/1_mb_file').with_size(1).build()

        the_file = file_reader.FileReader().read('build/test_data_1_mb_file')
        assert_equal(the_file.size(), 1)
