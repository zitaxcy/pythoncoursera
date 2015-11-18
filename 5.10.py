Summary = 0.0
Count = 0.0
while Ture
	Number = raw_input("Enter a number:")
	if Number = "Done":
		break
	else:
		try:
			Summary = summary + float(Number)
			Count = Count + 1.0
		except:
			print "Please enter a numerical number"
Average = Summary / Count
print "The Summary of input is ", Summary
print "The number of input is", Count
print "The average of input is", Average