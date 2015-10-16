import os
import sys
import data_builder
from nose.tools import assert_equal
from bobbadilla import file_reader

sys.path.append(os.path.abspath(".."))


def test_read_size_of_a_1_mb_file():
        data_builder.FileBuilder().with_path(
            'build/test_data/1_mb_file').with_size(1).build()

        the_file = file_reader.read_file('build/test_data/1_mb_file')
        assert_equal(the_file['size'], 1)


def test_size_of_non_existing_file_returns_None():
        the_file = file_reader.read_file(
            'build/test_data/non_existing')
        assert_equal(the_file, None)
