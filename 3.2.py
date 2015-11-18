Score = raw_input("Enter Score:")
if Score > 1.0:
	print "Bad score"
else:
	if Score >= 0.9:
		print "A"
	elif Score >= 0.8:
		print "B"
	elif Score >= 0.7:
		print "C"
	elif Score >= 0.6:
		print "D"
	elif Score < 0.6:
		print "E"