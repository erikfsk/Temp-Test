import re

s = "2.2.22"

f = re.findall("\.",s)

print len(f)

if f< 0 or f>0:
	print "success"