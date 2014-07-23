""" Problem 1 - Create a list with the items: three, two, one """
foo_list = ["three", "two", "one"]
print foo_list
""" Problem 2 - Iterate over the list and print "three, two, one, let's jam." 
on a single line. """


empty_foo = " "
for index, char in enumerate(foo_list):
    if char != foo_list[-1]:
        empty_foo += char + ", " 
    if char == foo_list[-1]:
        empty_foo += char
        print empty_foo + ", let's jam."
    

# Problem 3 - Create a dict called body with the following key value pairs: 
# head=10, torso=10, legs=10

body = {"head": 10, "torso": 10, "legs": 10}


# Problem 4 - Create a function called damage_player with the function signature 
# (body_dict, body_part, damage). Inside the function use the string contained in 
# body_part as the key to body_dict and adjust the value based on how much damage
# is done. return body_dict after it has been modified. Call the function like so 
# using the dict made in problem 3:

def damage(body_dict, body_part, damage):
    body_dict[body_part]-=damage
    return body_dict
    

body = damage(body, 'head', 5)
print body

# hint you can use the += and -= in python just like most languages to avoid 
# expressions like x = x + 1 with x += 1 instead.