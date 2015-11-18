filename = raw_input("Enter filename:")
fhand = open(filename)
Confidence = 0.0
count = 0.0
for line in fhand:
	if line.startswith("X-DSPAM-Confidence:"):
		start = line.find(":")
		end   = len(line)
		Confidence = Confidence + float(line[start+2:end-1])
		count = count + 1
AvCon = Confidence / count
print "Average spam confidence:", AvCon

#fhand = open("C:/Users/Ying/test-repo/pythoncoursera/mbox-short.txt")
#for line in fhand:
#	line = line.upper()
#	print line