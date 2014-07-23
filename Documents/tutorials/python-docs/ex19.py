# defining a function called cheese_and_crackers that takes 2 parameters
def cheese_and_cracker(cheese_count, boxes_of_crackers):
	# prints out a txts that interpolates with the cheese count
	print "You have %d cheeses!" % cheese_count
	# prints out a txts that interpolates with the boxes of crackers
	print "You have %d boxes of crackers" % boxes_of_crackers
	# simplt prints out a line of txt's 
	print "Man that's enough for a party!"
	# prints a line of txt's that has a  "\n" at the end w/means "next new line"
	print "Get a blanket.\n"

# NOTE THAT EVERY TIME THE FUNCTION IS CALLED IT RE-DO ITS SELF AGAIN


# prints out a line of txt's 
print "We can just give the function numbers directly:"
# calls the so called defined function above given with two integers as a parameters
cheese_and_cracker(20, 30)

# prints out a line of txt's
print "OR, we can use variables from our script:"
# declared two variables assigned each with integers
amount_of_cheese = 10
amount_of_crackers = 50
# calls the function again now with two parameters w/is the declared variables on ealier lines
cheese_and_cracker(amount_of_cheese, amount_of_crackers)

# prints out a line of txt's
print "We can even do math inside too:"
# calls the function again with two parameters now doing addition on each parameter
cheese_and_cracker(10 + 20, 5 + 6)

# prints out a line of txt's
print "And we can combine the two, variables and math:"
# calls the function again combining the variables and math procedure as its parameters
cheese_and_cracker(amount_of_cheese + 100, amount_of_crackers + 1000)

