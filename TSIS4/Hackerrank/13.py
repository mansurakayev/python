from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*i)) for i in attrs]
n = int(input())
html=""
for _ in range(n):
    text = input()
    html+= text
    html+="\n"
parser = MyHTMLParser()
parser.feed(html)
parser.close()