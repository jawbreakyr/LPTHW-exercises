"""
seek(),open(), .name
"""


foo = open("txtlines.txt", "rw+")
bar = foo.read()
print bar
print "this is the file name %s" %foo.name


foo.seek(0, 0)

line = foo.readline()
print "Read Line: %s" %(line)



line = foo.readline()
print "Read Line: %s" %(line)


print foo.name

foo.close()