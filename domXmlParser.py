__author__ = 'arshad'
import xml.dom.minidom

#parse, documentElement , hasAttribute, getAttribute, getElementsByTagName,
from xml.dom.minidom import parse

DOMTreeParser = parse("movies.xml")
print DOMTreeParser

collection = DOMTreeParser.documentElement
print 'Collection: ', collection

if collection.hasAttribute("shelf"):
    print "Root Element : %s" % collection.getAttribute("shelf")

moviesDom = collection.getElementsByTagName("movie")
print 'movies DOM coll: ', moviesDom


for movieDom in moviesDom:
    if movieDom.hasAttribute('title'):
        print 'Movie Title: ', movieDom.getAttribute('title')
    typeDom = movieDom.getElementsByTagName("type")[0]
    print 'Type: %s ' % typeDom.childNodes[0].data


print 'direct printing: ', collection.getElementsByTagName('movie')[1].getElementsByTagName('format')[0].childNodes[0].data
