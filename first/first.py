"""
The first problem:
    the words of 2**23 is written on the paper
"""
def findfirst(path):
    newp = 2**38
    newpath = path+'/'+str(newp)+'.html'
    return newpath

if __name__=="__main__":
    path = "http://www.pythonchallenge.com/pc/def/0.html"
    frontpath = path[:path.rfind('/')]
    print findfirst(frontpath)
