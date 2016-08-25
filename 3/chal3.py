#Opens symbols file
f = open("chal4Symbols.txt")

#Assigns content of symbols file to variable
symbols = f.read()

#Rows are 81 characters long
#print symbols[0]
#print symbols[81]
#print symbols

result = ""

i=0
for symbol in symbols:
	if (i > 3):
		if symbol.islower():
			if not (i%81 > 77) or not (i%81 < 2):
				#result += symbol
				if (symbols[i-3].isupper() and 
					symbols[i-2].isupper() and 
					symbols[i-1].isupper() and 
					symbols[i+1].isupper() and 
					symbols[i+2].isupper() and 
					symbols[i+3].isupper()):
					if not (symbols[i - 4].isupper()) and not (symbols[i+4].isupper()):
						result += symbol
	i +=1
print result




#IGNORE ALL THIS. I WAS DOING IT ALL WRONG
#i=0
# for symbol in symbols:
	# NumOfBodyguardsToFind = 0
	# if symbol is "y":
		# #Check is symbol is lowercase
		# if symbol.islower():
			# #Check if letter to left exists
			# if not(i%81 is 0):
				# #Letter exists to left, so check it
				# if symbols[i-1].isupper():
					# #print "symbol to left is %s" % str(symbols[i-1])
					# NumOfBodyguardsToFind +=1
			
			# #Check if letter to right exists
			# if not(i%79 is 0) and (i+1 < len(symbols)):
				# #Letter exists to left, so check it
				# if symbols[i+1].isupper():
					# #print "symbol to right is %s" % str(symbols[i+1])
					# NumOfBodyguardsToFind +=1
			
			# #Check above letter (If not on top row)
			# if i >= 81:
				# if symbols[i-81].isupper():
					# #print "symbol to north is %s" % str(symbols[i-81])
					# NumOfBodyguardsToFind +=1
			
			# #Check below letter (If not on bottom row)
			# if not i+81 > len(symbols):
				# if symbols[i+81].isupper():
					# #print "symbol to south is %s" % str(symbols[i+81])
					# NumOfBodyguardsToFind +=1
	
	# if NumOfBodyguardsToFind is 3:
		# result += symbol
	
	# i += 1