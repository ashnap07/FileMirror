import hashlib
import time
import sys

mainFile=sys.argv[1]
backupFile=sys.argv[2]

def getHash(filePath):
    file=open(filePath,"r")
    lines=file.readlines()
    file.close()
    hash=hashlib.md5(str(lines).encode()).hexdigest()
    return hash
    
def isEqualHash(file1,file2):
    return getHash(file1)==getHash(file2)
    

def copyFile(source,dist):
    file=open(source,"r")
    lines=file.readlines()
    file.close()
    file2=open(dist,"r+")
    file2.truncate(0)
    file2.writelines(lines)
    file2.close
    
while True:  
    if not isEqualHash(mainFile,backupFile):
        copyFile(mainFile,backupFile)
        print("changes saved to the backup!")
    else:
        print("no changes!")
    time.sleep(5)
