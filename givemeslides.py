#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import argparse
parser = argparse.ArgumentParser()
from html5slides import get_html_element


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
    html = get_html_element(args)
    print "<!DOCTYPE html>\n\n%s" % html


if __name__ == '__main__':
    main()
