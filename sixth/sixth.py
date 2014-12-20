"""
The first problem:(peak->pickle)
    channel.html -> channel.zip -> download
"""
import urllib
import zipfile


filepath='channel'

def findsixth(filename):
    filefd = open(filepath+'/'+filename,'r')
    lines = filefd.readlines()
    filefd.close()
    data = filter(str.isdigit,lines[0])
    print data
    if data:
        findsixth(data+'.txt')
    else:
        print lines[0]
    
def findsixthagain(zipfile,filename):
    filefd = open(filepath+'/'+filename,'r')
    lines = filefd.readlines()
    filefd.close()
    data = filter(str.isdigit,lines[0])
    print zipfile.getinfo(filename).comment,
    if data:
        findsixthagain(zipfile,data+'.txt')
    else:
        print lines[0]
        
if __name__=="__main__":
    # start from 90052
    findsixth('90052.txt')
    # hit: Collect the comments, zipfile has comment
    z = zipfile.ZipFile('channel.zip')
    findsixthagain(z,'90052.txt')
    # hockey.html
