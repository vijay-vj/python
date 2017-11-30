from html.parser import HTMLParser
 
metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print ("Encountered COmment: ", data)
        pos = self.getpos()
        print ("At line ", pos[0], " Position ", pos[1])
    
    def handle_endtag(self,data):
        print ("Encountered End tag: ", data)
        pos = self.getpos()
        print ("At line ", pos[0], " Position ", pos[1])
    
    def handle_data(self,data):
        print ("Encountered Data: ", data)
        pos = self.getpos()
        print ("At line ", pos[0], " Position ", pos[1])
    
    def handle_starttag(self,tag, attrs):
        global metacount
        print ("Encountered Start Tag: ", tag)
        if tag == "meta":
            metacount += 1
        pos = self.getpos()
        print ("At line ", pos[0], " Position ", pos[1])

 
def main():
    Parser =MyHTMLParser()
    f = open("samplehtml.html")

    if f.mode == 'r':
        contents = f.read()
        #parser.feed('<html><head><title>Test</title></head>'
        #    '<body><h1>Parse me!</h1></body></html>')
        Parser.feed(contents) 

    print ("Meta count is: {} time " .format(metacount))     


if __name__ == "__main__":
    main()