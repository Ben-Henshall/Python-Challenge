import glob, os
import re

#test = glob.glob('channel/*.txt')



# for file in test:
	# file_num = re.findall(r"\d+", file)
	# if file_num:
		# file_num = file_num[0]
		# print file_num
	# #print(file)
	
	

pathprefix = "channel/"
	
nothing = 90052	#Start Nothing

#CHANGE TO TRUE TO DO FIRST CYCLE
while False:
	path = pathprefix + str(nothing) + ".txt"
	#print path
	file = open(path, "rb")
	result = file.read()
	print result
	result_split = re.findall(r"\d+", result)
	#print result_split
	if (result_split.count > 0):
		nothing = result_split[0]

dictComment = {}
while True:
	path = pathprefix + str(nothing) + ".txt"
	#print path
	file = open(path, "rb")
	result = file.read()
	#print result
	result_split = re.findall(r"\d+", result)
	#print result_split
	comment = re.findall(r"[aA-zZ]+", result)
	print comment
	
	for commentSection in comment:
		if not commentSection in dictComment:
			dictComment[commentSection] = 1
		else:
			dictComment[commentSection] += 1
	
	if (result_split != []):
		nothing = result_split[0]
	else:
		print "\n\n"

		for commentRef in dictComment:
			if dictComment[commentRef] > 1:
				print commentRef, dictComment[commentRef]
		break



if True:
	#Collecting comments?
	path_list = glob.glob('channel/*.txt')

	dictCount = {}
	dictPath = {}
	for path in path_list:
			file = open(path, "rb")
			result = file.read()
			result_split = re.findall(r"\d+", result)
			print path, result_split
			if result_split:
				if not result_split[0] in dictCount:
					dictCount[result_split[0]] = 1
				else:
					dictCount[result_split[0]] += 1
					
				if not (int(result_split[0]) / 2) in dictCount:
					dictCount[result_split[0]] = 1
				else:
					dictCount[result_split[0]] += 1
					
			if not path in dictPath:
				dictPath[path] = 1
			else:
				dictPath[path] += 1
					
	print "\n\n\n"

	#Checking if there are any duplicate file names
	for path in dictPath:
		if dictPath[path] > 1:
			print dictPath[path]
				
	for num in dictCount:
		if dictCount[num]:
			print dictCount[num]