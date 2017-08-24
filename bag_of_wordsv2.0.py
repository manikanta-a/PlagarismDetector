from itertools import chain
from glob import glob
import string
import os
import math
import re

def frequence(filename):
	#words_to_lower(filename)

	lst = words_to_list(filename)
	#print(lst)
	#lst = remove(lst)
	dic = {}
	for word in lst:
		if word in dic:
			dic[word]=dic[word]+1
		else:
			dic[word] = 1
	dic = remove_space(dic)
	return dic

# def words_to_lower(filename):
# 	file = open(filename,"r")
# 	lines = [line.lower() for line in file]
# 	with open(filename, 'w') as out:
# 		out.writelines(lines)

# 	return file

def words_to_list(filename):
	#self.filename = filename
	lst = []
	original_string = open(filename).read()
	new_string = re.sub('[^a-zA-Z0-9\n]', ' ', original_string)
	open('temp.txt', 'w').write(new_string)
	file1 = open(filename,'r')
	for line in file1:
		lst.extend(line.lower().split())

	return lst

# def remove(lst):

# 	templst = [word.strip(string.punctuation) for word in lst]

# 	return templst

def remove_space(dictionary):
	if '' in dictionary:
		del dictionary['']
	return dictionary

def dot_product(d1 = {},d2 = {}):
	dotresult  = {}
	for x in d1:
		if x in d2:
			dotresult[x] = d1[x] * d2[x]

	for y in d2:
		if y in d1:
			dotresult[y] = d2[y]*d1[y]

	return dotresult

def sum_dotproduct(d1 = {}):
	total = sum(d1.values())
	return total

def square_dictvalues(d1 = {}):
	total = 0
	for x in d1:
		total = total+ d1[x]**2
	#total = sum(d1.values())
	return total

def similarity_function(a,b,c):

	result = a/((b**(0.5))*(c** (0.5)))

	return result#round(result,2)

# file1 = open("Test.txt","r")
# lines = [line.lower() for line in file1]
# with open('Test.txt', 'w') as out:
#      out.writelines(sorted(lines))

def bag_of_words(path):
	pathlist = [p for p in os.listdir(path) if p.endswith('.txt') and p != "temp.txt"]
	#print(pathlist)
	os.chdir(path)
	matrix2 = []

	for i in range(len(pathlist)):
		matrix = []
		file1 = frequence(pathlist[i])
		for j in range(len(pathlist)):
			filess1 = 0
			file2 = frequence(pathlist[j])
			res = dot_product(file1,file2)
			sumi = sum_dotproduct(res)
			filess1 = square_dictvalues(file1)
			filess2 = square_dictvalues(file2)
			final = similarity_function(sumi,filess1,filess2) * 100.0
			matrix.append(round(final,2))
		matrix2.append(matrix)

	return matrix2


# file1 = frequence('Comands for github.txt')
# print(file1)

# file2 = frequence('Comands for github.txt')

# print(file2)

# res = dot_product(file1,file2)

# print("res =",res)

# sumi = sum_dotproduct(res)

# filess1 = square_dictvalues(file1)

# filess2 = square_dictvalues(file2)

# print(sumi,filess1,filess2)

# print(similarity_function(sumi,filess1,filess2))
user_input = input("Please enter the path for comparison : ")

final_result = bag_of_words(user_input)

listoffiles = [p for p in os.listdir(user_input) if p.endswith('.txt')]

listoffiles = ["      "]+listoffiles

#print(listoffiles)

# for x in listoffiles:
# 	print(x,"   ",end='')


for  x in  range(len(final_result)):
	for y in range(len(final_result[x])):
		print(final_result[x][y], "   ",end='')
	print("\n")
#print(test)