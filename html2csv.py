import sys
f = open(sys.argv[1],"r") 
fout = open("report_Parking.csv","w") 
CSVrow=""
finished = False
oddLine = True
for line in f:
	if line.find("Test Module Information")>-1:
		break
	if (line.find("SysTst_")>-1 and not line.find("_SysTst_")>-1 or line.find("fail")>-1 and not line.find("failed")>-1 or line.find("pass")>-1 and not line.find("passed")>-1):
		line = line.split("<")[1]
		line = line.split("\"")[2]
		CSVrow += line.split(">")[0] + line.split(">")[1]
		#CSVrow += line.split(">")[1][2]
		if oddLine:
			CSVrow += ","
			oddLine = False
		else:
			CSVrow += "\n"
			oddLine = True
fout.write(CSVrow)
f.close
fout.close