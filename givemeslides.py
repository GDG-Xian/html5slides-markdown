#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import argparse
parser = argparse.ArgumentParser()
from html5slides import get_slides


def prepare():
    parser.add_argument("file",
                    help="file to parse",
                    type=str,
                    action="store")
    parser.add_argument("--theme",
                    help="theme to use, if not provided, default theme will be used",
                    type=str,
                    action="store")
    parser.add_argument("--offline",
                    help="If you use this flag, you can get offline js files and css files",
                    action="store_true")


def main():
    prepare()
    args = parser.parse_args()
    print get_slides(args)


if __name__ == '__main__':
    main()
