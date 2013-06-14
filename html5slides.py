import sys
from markdown2 import markdown
from BeautifulSoup import BeautifulSoup, Tag


def get_file_contents(filename):
    try:
        f = open(filename, 'r')
        contents = f.read()
        f.close()
    except Exception, e:
        print "Please check %s" % filename
        sys.exit(1)
    return contents


def get_html_element(args):
    contents = get_file_contents(args.file)
    soup = BeautifulSoup(markdown(contents))

    hsoup = BeautifulSoup()
    html = Tag(hsoup, 'html')
    hsoup.append(html)

    head = Tag(hsoup, 'head')
    title = Tag(hsoup, 'title')
    title.setString(args.file)
    head.append(title)

    link = Tag(hsoup, 'link')
    link['rel'] = 'stylesheet'
    link['type'] = 'text/css'
    if args.offline:
        link['href'] = 'default.css'
    else:
        link['href'] = 'http://gdg-xian.github.io/html5slides-markdown/themes/default.css'
    head.append(link)

    script = Tag(hsoup, 'script')
    if args.offline:
        script['src'] = 'html5slides.js'
    else:
        script['src'] = 'http://gdg-xian.github.io/html5slides-markdown/javascripts/html5slides.js'
    head.append(script)
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

    return html
