#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
import argparse
parser = argparse.ArgumentParser()
from markdown2 import markdown
from BeautifulSoup import BeautifulSoup, Tag


def prepare():
    parser.add_argument("file",
                    help="file to parse",
                    type=str,
                    action="store")
    parser.add_argument("--theme",
                    help="theme to use, if not provided, default theme will be used",
                    type=str,
                    action="store")


def create_head_elem(title, soup):
    head = Tag(soup, 'head')
    head.append(Tag("title"))
    head.insert(Tag("script"))
    return head


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

    soup = BeautifulSoup(markdown(contents))

    hsoup = BeautifulSoup()
    html = Tag(hsoup, 'html')
    hsoup.append(html)

    head = Tag(hsoup, 'head')
    title = Tag(hsoup, 'title')
    h1 = soup.find('h1')
    title.setString(h1.text)
    h1.extract()
    head.append(title)

    script1 = Tag(hsoup, 'script')
    script1['src'] = 'html5slides.js'
    head.append(script1)
    script2 = Tag(hsoup, 'script')
    script2['src'] = 'prettify.js'
    head.append(script2)
    html.append(head)

    body = Tag(hsoup, 'body')
    for h3 in soup.findAll('h3'):
        tag = Tag(hsoup, "article")
        body.append(tag)
        tag.append(h3)
    html.append(body)

    try:
        f = open('test.html', 'w')
        f.write(html.prettify())
        f.close()
    except Exception, e:
        #print "Something wrong, %s" % e
        sys.exit(1)


if __name__ == '__main__':
    main()
