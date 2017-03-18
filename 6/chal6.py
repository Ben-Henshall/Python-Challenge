import zipfile
import re
comments = ""
fileToCheck = "90052"

#Open zip archive
zip = zipfile.ZipFile("channel.zip", "r")
#CHANGE TO TRUE TO DO FIRST CYCLE
endOfFile = False
while endOfFile == False:
	#format text file name
	path = fileToCheck + ".txt"
	#add comment to our comment string
	comments += zip.getinfo(path).comment
	
	#get the file contents so we know which file to check next
	fileContents = zip.read(path)
	
	#remove extra characters, we only want the int pointer
	result = re.findall(r"\d+", fileContents)
	
	#Check to see if we've reached the end
	if (len(result) != 0):
		fileToCheck = result[0]
	else:
		#we're at the end, exit the loop
		endOfFile = True
				
print comments