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
    title.setString(args.file)
    head.append(title)

    script1 = Tag(hsoup, 'script')
    script1['src'] = 'html5slides.js'
    head.append(script1)
    script2 = Tag(hsoup, 'script')
    script2['src'] = 'prettify.js'
    head.append(script2)
    html.append(head)

    body = Tag(hsoup, 'body')
    body['style'] = 'display:none'
    section = Tag(hsoup, 'section')
    section['class'] = 'slides layout-regular template-default'
    body.append(section)
    elements = []
    elements.append(soup.first())
    elements.extend(soup.first().findNextSiblings())
    article = Tag(hsoup, 'article')
    section.append(article)
    for element in elements:
        if element.name == 'hr':
            article = Tag(hsoup, 'article')
            section.append(article)
        else:
            article.append(element)

    html.append(body)

    print html


if __name__ == '__main__':
    main()
