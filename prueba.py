programname = 'prueba'

import getopt
import sys
import glob
import os

if __name__ == "__main__":
    try: # Put getopt in place for future usage.
        opts, args = getopt.getopt(sys.argv[1:],None)
    except getopt.GetoptError:
        print usage(sys.argv[0])  # print help information and exit:
        sys.exit(2)
    if len(args) == 0:
        print usage(sys.argv[0])  # print help information and exit:
        sys.exit(2)       
    print programname
    html_files = glob.glob(args[0])
    for htmlfilename in html_files:
        outputfilename = os.path.splitext(htmlfilename)[0]+'.csv'
        
        print 'Reading %s, writing %s...' % (htmlfilename, outputfilename)
        try:
            htmlfile = open(htmlfilename, 'rb')
            csvfile = open( outputfilename, 'w+b')
            data = htmlfile.read(8192)
            while data:
                if data.find("PositiveResultCell")>-1:
                    print data
                    print ","
                    csvfile.write(data)
                data = htmlfile.read(8192)
            csvfile.close()
            htmlfile.close()
        except:
            print 'Error converting %s        ' % htmlfilename
            try:    htmlfile.close()
            except: pass
            try:    csvfile.close()
            except: pass
    print 'All done.                                      '