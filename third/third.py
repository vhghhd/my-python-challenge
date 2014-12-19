"""
The third problem:
    recognize the characters. maybe they are in the book,
    but MAYBE they are in the page source.
    find rare characters in the mess below.
"""
def findthird(path):
    filefd = open('third.txt',"r")
    lines = filefd.readlines()
    result = []
    for line in lines:
        data = filter(str.isalpha,line)
        if data:
            result.append(data)
    return path+'/'+''.join(result)+'.html'

if __name__=="__main__":
    path = "http://www.pythonchallenge.com/pc/def/0.html"
    frontpath = path[:path.rfind('/')]
    print findthird(frontpath)
