Hours = raw_input("Enter Hours:")
Rate = raw_input("Enter Rate:")
Work = raw_input("Enter payment of one hour:")
try:
if float(Hours) <= 40:
	Pay = float(Hours) * float(Rate) * float(Work)
else :
	Pay = float(Hours) * 1 * float(Work)
print Pay
except:
	print "Error, please enter numeric input"