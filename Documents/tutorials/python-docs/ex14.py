from sys import argv

user_name, script = argv[1:]
prompt = '> '
sex = '>>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What is your gender %s?" % user_name
gender = raw_input(sex)

if gender == "male" or gender == "Male":
    print """
    Alright, so you said %r about liking me.
    You live in %r. Not sure where that is.
    And you have %r computer. And you are a %r.
    Get lost.
    """ % (likes, lives, computer, gender)
    
elif gender == "female" or gender == "Female":
    print """
    Alright, so you said %r aout liking me.
    You live in %r. Not sure where that is.
    And you have %r computer. And you are a %r.
    Show Boobs!
    """ % (likes, lives, computer, gender)
    
else:
    print "Fuck off"
