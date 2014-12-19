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
    htmlfront = html[:html.rfind('/')]
    print htmlfront
    print urllib.urlopen(html).read()

if __name__=="__main__":
    path = "http://www.pythonchallenge.com/pc/def/0.html"
    frontpath = path[:path.rfind('/')]
    jumptorealanswer(findforth(frontpath))
