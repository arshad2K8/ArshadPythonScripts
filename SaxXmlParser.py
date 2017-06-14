__author__ = 'arshad'
# SAX API  , event driven parsing , own Content Handler

# startElement called for every start of tag, endElement for end of element,
import xml.sax
class MoviesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentTag = ""
        self.type = ""
        self.format =""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    #call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentTag = tag
        if tag == "movie":
            print "*** MOvie ***"
            title = attributes['title']
            print "Title: ", title

    def endElement(self, tag):
        if self.CurrentTag == "type":
            print "Type: ",self.type

    def characters(self, content):
        if self.CurrentTag == "type":
            self.type = content



if ( __name__ == "__main__"):
    #1. create xml sax parser object
    parser = xml.sax.make_parser()
    #turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    #create our own  context handler
    Handler = MoviesHandler()
    #override default context handler
    parser.setContentHandler( Handler )
    parser.parse("movies.xml")

