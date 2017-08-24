def words_to_list(file):
	#file = file
	lst = []
	read = open(file,'r')
	#print(read)
	for line in read:
		lst.extend(line.split())
	return lst
		#for word in line:



print(words_to_list("file1.txt"))