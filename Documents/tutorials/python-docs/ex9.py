# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

"""concatenating using "," while
interpolating at the same time 
calls an error line"""
print "Here are the days: %s" % days
#interpolating using "%r" sure prints the raw input 
print "Here are the months: %r" % months

print """
There's somethong going on here.
With the three doubble-qoutes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""