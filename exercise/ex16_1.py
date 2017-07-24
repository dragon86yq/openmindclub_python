# study drill
from sys import argv
script, filename = argv
print("We're going to read  %r."%filename)
txt = open(filename,'r')
print("Starting to read the file")
content = txt.read()
print("the content of file is %r " % content)