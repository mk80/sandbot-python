from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        print(data)

try:
    input_file = sys.argv[1]
except:
    print("please provide input file...")
    sys.exit()

parser = MyHTMLParser()

with open(input_file, 'r') as f:
    file_data = f.read()

parser.feed(file_data)

exit
