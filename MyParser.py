import os.path

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
outputfilename = os.path.splitext("report_Parking.html",)[0]+'.csv'

print 'Reading %s, writing %s...' % ("report_Parking.html", outputfilename)
        
try:
    htmlfile = open("report_Parking.html", 'rb')
    csvfile = open( outputfilename, 'w+b')
    data = htmlfile.read(8192)
    while data:
        parser.feed( data )
        csvfile.write( parser.getCSV() )
        sys.stdout.write('%d CSV rows written.\r' % parser.rowCount)
        data = htmlfile.read(8192)
    csvfile.write( parser.getCSV(True) )
    csvfile.close()
    htmlfile.close()
except:
    print 'Error converting %s        ' % "report_Parking.html"
    try:    htmlfile.close()
    except: pass
    try:    csvfile.close()
    except: pass