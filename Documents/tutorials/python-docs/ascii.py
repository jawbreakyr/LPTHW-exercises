"""
a simple asciii decoder not perfect but readable (least for me)
"""





"""
K -> M
O -> Q
E -> G

g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj.
"""


letters = "map"
		 # i hope you didnt tr{nsl{te it |y h{nd0 th{ts wh{t computers {re for0 doing it in |y h{nd is inefficient {nd th{t)s why this text is so long0 using string0m{ketr{ns*+ is recommended0 now {pply on the url0

new_word= []

for letter in letters:
	if letter == " ":
		new_word.append(" ")

	else:
		code = ord(letter)
		new_word.append(chr(code+2))

print "".join(new_word)





