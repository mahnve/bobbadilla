#!/usr/bin/env python

import sys
import argparse
import random
import shutil


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('m3u',
                        help="m3u playlist file(s)")
    parser.add_argument("--output-dir",
                        nargs=1,
                        help="where to write files")
    parser.add_argument("--no-of-songs",
                        nargs='?',
                        help="number of songs to copy from playlist")
    parser.parse_args(args)


def main(*args):
    parsed = parse_args(args)
    lines = get_random_lines(read_m3u_file(parsed.m3u))
    copy_files(lines, parsed.output_dir)


def read_m3u_file(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def get_random_lines(lines, no_of_lines):
    return random.sample(lines, no_of_lines)


def copy_files(file_names, output_dir):
    for f in file_names:
        shutil.copyfile(f, output_dir)

main(sys.argv)
