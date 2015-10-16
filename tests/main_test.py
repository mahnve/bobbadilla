import data_builder
import sys
import os
from nose.tools import assert_equal
from bobbadilla import file_reader

sys.path.append(os.path.abspath(".."))


def test_empty_m3u():
    m3u = data_builder.m3uBuilder().build()
    assert_equal(m3u, [])


def test_size_of_non_existing_file_returns_None():
    the_file = file_reader.read_file('build/test_data/non_existing')
    assert_equal(the_file, None)
