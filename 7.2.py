fhand = open("C:/Users/Ying/test-repo/pythoncoursera/mbox.txt")
print fhand

count = 0
for line in fhand:
	count = count + 1
print 'Line Count:', count

inp = fhand.read()
print len(inp)

for line in fhand:
	line = line.rstrip()
	if line.startswith("From:"):
		print line

for line in fhand:
	line = line.rstrip()
	if not line.startswith("From:"):
		continue
	print line
	
for line in fhand:
	line = line.rstrip()
	if line.find("@uct.ac.za") == -1：
		continue
	print line
	
fname = raw_input("Enter the file name:")
try:
fhand = open(fname)
except:
	print "File cannot be opened", fname
	print "Please Enter file name with address like *:/**/**.** ,ex:C:/user/mobi.txt"count = 0
	exit()
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print 'Subject Line Count:', count
