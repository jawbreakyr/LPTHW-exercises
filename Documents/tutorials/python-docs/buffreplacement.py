marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."




buffer = ''
replaced = ''
for index, char in enumerate(line):
	if char != ' ':
		buffer += char
	if buffer == marker:
		replaced += replacement
		buffer = ''
	if char == ' ':
		if buffer:
			replaced += buffer
			buffer = ''
		replaced += char
	if len(line) == (index + 1) and buffer:
		replaced += buffer

print replaced
