"""
The first problem:(peak->pickle)
    the banner.p in the peak.html source code
"""
import urllib
import pickle

def findfifth(html):
    data = urllib.urlopen(html).read()
    return data

if __name__=="__main__":
    path = "http://www.pythonchallenge.com/pc/def/0.html"
    frontpath = path[:path.rfind('/')]
    # print findfifth(frontpath+'/peak.html')
    # hit1: banner.p
    binstr = findfifth(frontpath+'/banner.p')
    data = pickle.loads(binstr)
    # first
    for dt in data:
        tmp = ''
        for d in dt:
            tmp += str(d[0]*d[1])
        print tmp
    # second
    for dt in data:
        print ''.join(map(lambda x:x[0]*x[1],dt))
