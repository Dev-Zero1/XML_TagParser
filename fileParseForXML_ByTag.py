import os
from xml.dom import minidom
import time

path = "C://Python//Scripts//data//xml//"
path2 = "C://Python//Scripts//compiledData//"
fileType = ".xml"

os.remove((path2+'data.txt'))
time.sleep(2)
##dir_list = os.listdir(path)

writeFile = open((path2+'data.txt'),"a")
processed = 0

##print("Files and directories in '",path,"' :")

for filename in os.listdir(path):
    if not filename.endswith(fileType): continue
    fullname = os.path.join(path, filename)
    print(filename)
    print("-----------------------------")
    print("-----------------------------")
    file = minidom.parse(fullname)
    models = file.getElementsByTagName('map')
    for elem in models:
        print(elem.firstChild.data)
        writeFile.write(elem.firstChild.data + ",/n")
        processed+=1
print("-----------------------------")        
print(str(processed) + ' Files processed')        
writeFile.close()
    
