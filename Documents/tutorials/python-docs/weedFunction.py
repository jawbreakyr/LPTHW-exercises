import random


def funct_n():
	return random.randrange(1,11)




def weeds_to_puff(bag_a_weed, sticks_a_bag):
	print "We got a %r bag of weeds." % bag_a_weed
	print "Each bag can make %r sitcks of weed." % sticks_a_bag
	print "With %r bag of weeds we can make %r sticks out of it." % (bag_a_weed, bag_a_weed*sticks_a_bag)
	print "Now its all we can puff.\n"

print "Assigning the amounts to each parameter."
weeds_to_puff(2 ,10)


print "Assigning the amounts to each parameter thru variables."
weed_bag_count = 4
sticks_each_bag = 20

weeds_to_puff(weed_bag_count, sticks_each_bag)


print "Assigning the amounts to each parameter while doing math operation."
weeds_to_puff(150 + 5, 20 + 30)


print "Assigning the amount for each parameter thru adding variables and integer."
weeds_to_puff(weed_bag_count + 10, sticks_each_bag + 20)


print "Assigning the amount for each parameter thru variables while doing math operation."
weeds_bag_counts = 4 + 8
sticks_each_bags = 20 + 3

weeds_to_puff(weeds_bag_counts, sticks_each_bags)

print "Experimental assigning of value to each param."
wack = weed_bag_count * weeds_bag_counts
kwack = sticks_each_bag * sticks_each_bags

weeds_to_puff(wack, kwack)

print "Assignning amounts to each param using the raw_input() & int()function."
foo = int(raw_input("bag count:"))
bar = int(raw_input("stick count:"))

weeds_to_puff(foo, bar)


print "Assignning amounts to each param using the raw_input() & int() function with math operation."
foo = int(raw_input("bag count:"))
bar = int(raw_input("stick count:"))

weeds_to_puff(foo + 10, bar + 20)


print "Experimental sol."
weeds_to_puff(funct_n, weeds_bag_counts)
