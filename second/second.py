"""
The second problem:
    all the letters shift two
"""
import string
def findsecond(path):
    data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    # first idea
    result = []
    for dt in data:
        n = ord(dt)
        if dt is ' ' or dt is '.' or dt is "'" or dt is '(' or dt is ')':
            result.append(dt)
        else:
            result.append(chr(n+2>ord('z') and ((n-ord('a')+2)%26+ord('a')) or n+2))
    print ''.join(result)
    # second idea
    table1 = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
    print data.translate(table1,"")

    table = string.maketrans("map","ocr")
    return path+'/'+"map".translate(table,"")+'.html'

if __name__=="__main__":
    path = "http://www.pythonchallenge.com/pc/def/0.html"
    frontpath = path[:path.rfind('/')]
    print findsecond(frontpath)
