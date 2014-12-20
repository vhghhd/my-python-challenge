"""
The forth problem:
    One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    And then we should use liburl to jump next and next
"""
import re
import urllib
def findforth(path):
    filefd = open('forth.txt','r')
    lines = filefd.readlines()
    data = ''.join(lines)
    msg = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', data)
    return path+'/'+''.join(msg)+'.html'

def jumptorealanswer(html):
    htmlfront = html[:html.rfind('/')+1]
    data = urllib.urlopen(html).read()
    num = filter(str.isdigit,data)
    print num
    if num and int(num) < 100000000:
        jumptorealanswer(htmlfront+'/linkedlist.php?nothing='+num)
    else:
        print data

if __name__=="__main__":
    path = "http://www.pythonchallenge.com/pc/def/0.html"
    frontpath = path[:path.rfind('/')]
    jumptorealanswer(findforth(frontpath))
    # hit1: linkedlist.html
    jumptorealanswer(frontpath+'/linkedlist.php')
    # hit2: linkedlist.php?nothing=12345
    jumptorealanswer(frontpath+'/linkedlist.php?nothing=12345')
    # hit3: Yes. 16044 Divide by two and keep going.
    jumptorealanswer(frontpath+'/linkedlist.php?nothing='+str(16044/2))
    # hit4: There maybe misleading numbers in the 
    #       text. One example is 82683. Look only
    #       for the next nothing and the next nothing is 63579
    jumptorealanswer(frontpath+'/linkedlist.php?nothing='+str(63579))
    # http://www.pythonchallenge.com/pc/def/peak.html
    
