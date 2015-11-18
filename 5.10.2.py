Strings = raw_input("Enter a series of number:(use comma to divide each other)")
import string
count = 0
Numbers = Strings.split(",")
largest = None
smallest = None

for number in Numbers:
	if largest is None or float(number) > largest:
		largest = float(number)
	if smallest is None or float(number) < smallest:
		smallest = float(number)
print "The largest number of input:", largest
print "The smallest number of input:", smallest