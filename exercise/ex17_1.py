from sys import argv

from os.path import exists

script,from_file,to_file = argv

print("script is %r"%(script))
print("Copying from %s to %s"%(from_file,to_file))

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
out_file = open(to_file,'w')
out_file.write(indata)
out_file.close()
in_file.close()

# study drill
"""
linux下cat 命苦可以查看文件内容
windows下type命令可以查看文件内容
"""