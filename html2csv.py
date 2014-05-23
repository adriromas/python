import sys
import glob
import os

os.chdir(sys.argv[1])
if sys.argv[1]!="":
	print "List of generated files:\n"
	for file in glob.glob("*.html"):
	    f = open(file,"r") 
	    name = file+".csv"
	    print "- "+name+"\n"
	    fout = open(name,"w") 
	    CSVrow=""
	    listCSVrow=""
	    CSVrow2=""
	    finished = False
	    lineType = "ID"
	    for line in f:
	        if line.find("Test Module Information")>-1:
	            break
	        if (lineType == "ID" and line.find("SysTst_")>-1 and not line.find("_SysTst_")>-1 or 
	        	(lineType == "Result" and line.find("fail")>-1 and not line.find("failed")>-1) or 
	        	(lineType == "Result" and line.find("pass")>-1 and not line.find("passed")>-1)):
	            #print "0: "+line+"\n"
	            line = line.split("<")[1]
	            #print "1: "+line+"\n"
	            line = line.split("\"")[2]
	            #print "2: "+line+"\n"
	            line = line.split(">")[1]
	            CSVrow += line+"  "
	            if lineType=="ID":
	                CSVrow += ","	                
	            else:
	            	if lineType=="Result":
	                	CSVrow += "\n"
	            print lineType+" ->["+line+"]"+"\n"
	            if lineType=="ID":
	            	lineType="Result"
	            else:
	            	lineType="ID"
	    fout.write(CSVrow)
	    f.close
	    fout.close
else:
    print "Please specify the path where the report files are stored. Example of use >>>html2csv \"C:\\Reports"