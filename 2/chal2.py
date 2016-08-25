#Opens symbols file
f = open("chal3Symbols.txt")

#Assigns content of symbols file to variable
symbols = f.read()

#Dict used to store occurences
dictCount = {}

#Cycles through all the symbols 
for symbol in symbols:
	#If we haven't found this symbol before
	if not symbol in dictCount:
		#Add it to the dict
		dictCount[symbol] = 1
	else:
		#Else increment occurences
		dictCount[symbol] += 1

print dictCount

rareSymbols = []
for symbol in dictCount:
	#If symbol is rare
	if (dictCount[symbol] < 10):
		rareSymbols +=symbol

print rareSymbols

#FOLLOWING IS NEEDED TO GET CORRECT ORDER OF STRING
result = ""
#Cycles through all the symbols 
for symbol in symbols:
	#If it's a rare symbol then
	if symbol in rareSymbols:
		#Add it to the result
		result += symbol
	#Else do nothing

print result