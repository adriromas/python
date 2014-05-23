import urllib                                
sock = urllib.urlopen("report_Parking.html") 
htmlSource = sock.read()                       
sock.close()                                        
print htmlSource  