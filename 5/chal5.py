import pickle, pprint

pickle_file = open("chal5Banner.p")

objects = pickle.load(pickle_file)

result_str = ""
i = 0
for object in objects:
	print "OBJECT %s" %i
	print(object)
	i += 1


	for char,n in object:
		result_str += char*n
	result_str += "\n"

print result_str
