from html.parser import HTMLParser
html = ""
class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if('\n' in data):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self,data):
        if(data != '\n'):
            print(">>> Data")
            print(data)
n = int(input())
for i in range(n):
    html += input().rstrip()
    html += '\n'
#print(html)    
parser = MyHTMLParser()
parser.feed(html)
parser.close()