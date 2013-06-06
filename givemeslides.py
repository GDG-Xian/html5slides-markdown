#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import argparse
parser = argparse.ArgumentParser()
from markdown2 import markdown

def prepare():
    parser.add_argument("file",
                    help="file to parse",
                    type=str,
                    action="store")
    parser.add_argument("--theme",
                    help="theme to use, if not provided, default theme will be used",
                    type=str,
                    action="store")

def main():
    prepare()
    args = parser.parse_args()
    try:
        f = open(args.file, 'r')
        contents = f.read()
        f.close()
    except Exception, e:
        print "Please check %s" % args.file
        sys.exit(1)

    import xml.etree.ElementTree as ET
    root = ET.fromstring("<root>%s</root>" %markdown(contents))
    html = ET.Element("section")

    #import pdb
    #pdb.set_trace()

    h1 = root.find('h1')
    root.remove(h1)

    element = None
    for child in root:
        if child.tag == 'h3':
            element = ET.Element("article")
            html.append(element)
        if element is not None:
            element.append(child)

    try:
        f = open('test.html', 'w')
        f.write(ET.tostring(html, method="html"))
        f.close()
    except Exception, e:
        #print "Something wrong, %s" % e
        sys.exit(1)

if __name__ == '__main__':
    main()