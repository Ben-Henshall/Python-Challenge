#First off, find the offset betwen letters
letters = [["K", "M"], ["O", "Q"],["E","G"]]

i = 0
print(len(letters))
while (i < len(letters)): 
	offset = ord(letters[i][1])-ord(letters[i][0])
	printString = "Offset for pair %s is %s" %(i,offset)
	print(printString)
	i = i+1

#Then translate the sentence to a new sentence using the offset
sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

newSentence = ""
for char in sentence:
	if not char.isalpha():
		#Ignore spaces
		print("IGNORE PUNCTUATION")
		newSentence +=char
	else:
		newASCII = ord(char)+offset
		#If ASCII value goes outside of alphabet, take it back around to start
		if newASCII > 122:
			newASCII -= 26
		newChar = chr(newASCII)
		print("ADDED %s" % newChar)
		newSentence += newChar

print(newSentence)