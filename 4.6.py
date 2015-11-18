def culpay(Hours, Rate):
	if Hours > 40:
		Pay = Hours * Rate * 100
	else:
		Pay = Hours * 1 * 100
	print Pay

def compugrade(Score):
	if Score > 1.0:
		print "Bad Score"
	else:
		if Score > 0.9:
			print "A"
		elif Score > 0.8:
			print "B"
		elif Score > 0.7:
			print "C"
		elif Score > 0.6:
			print "D"
		elif Score <= 0.6:
			print "F"
		
