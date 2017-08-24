from itertools import chain
from glob import glob
import string
import os
import math
import re

class BOW(object):

	def frequence(self,filename):
		self.filename = filename
		lst = self.words_to_list(self.filename)
		dic = {}
		for word in lst:
			if word in dic:
				dic[word]=dic[word]+1
			else:
				dic[word] = 1
		dic = self.remove_space(dic)
		return dic


	def words_to_list(self,filename):
		self.filename = filename
		lst = []
		original_string = open(self.filename).read()
		new_string = re.sub('[^a-zA-Z0-9\n]', ' ', original_string)
		open('temp.txt', 'w').write(new_string)
		file1 = open(self.filename,'r')
		for line in file1:
			lst.extend(line.lower().split())

		return lst

	def remove_space(self,dictionary):
		self.dictionary = dictionary
		if '' in self.dictionary:
			del self.dictionary['']
		return self.dictionary

	def dot_product(self,d1 = {},d2 = {}):
		self.d1 = d1
		self.d2 = d2
		dotresult  = {}
		for x in self.d1:
			if x in self.d2:
				dotresult[x] = self.d1[x] * self.d2[x]

		for y in self.d2:
			if y in self.d1:
				dotresult[y] = self.d2[y]*self.d1[y]

		return dotresult

	def sum_dotproduct(self,d1 = {}):
		self.d1 = d1
		total = sum(self.d1.values())
		return total

	def square_dictvalues(self,d1 = {}):
		self.d1 = d1
		total = 0
		for x in self.d1:
			total = total+ self.d1[x]**2
		return total

	def similarity_function(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

		result = self.a/((self.b**(0.5))*(self.c** (0.5)))

		return result

	def bag_of_words(self,path):
		self.path = path
		pathlist = [p for p in os.listdir(self.path) if p.endswith('.txt') and p != "temp.txt"]
		#print(pathlist)
		os.chdir(self.path)
		self.matrix2 = []

		for i in range(len(pathlist)):
			self.matrix = []
			file1 = self.frequence(pathlist[i])
			for j in range(len(pathlist)):
				filess1 = 0
				file2 = self.frequence(pathlist[j])
				res = self.dot_product(file1,file2)
				sumi = self.sum_dotproduct(res)
				filess1 = self.square_dictvalues(file1)
				filess2 = self.square_dictvalues(file2)
				final = self.similarity_function(sumi,filess1,filess2) * 100.0
				self.matrix.append(round(final,2))
			self.matrix2.append(self.matrix)

		return self.matrix2

objBOW = BOW()

user_input = input("Please enter the path for comparison : ")

final_result = objBOW.bag_of_words(user_input)

listoffiles = [p for p in os.listdir(user_input) if p.endswith('.txt') and p != "temp.txt"]

length = len(listoffiles)

dislist = []

for i in range(1,length+1):
	dislist = dislist + ["file"+str(i)]
#print(dislist)



for i in range(length):
	
	print(dislist[i]," = ", listoffiles[i])


#listoffiles = ["      "]+listoffiles
flag = 0
c = 0
spaces = '      '
print("\n")
for  x in  range(len(final_result)):
	if flag == 0:
		print('  ',spaces*2,end='')
		for g in dislist:
			print(g,spaces*2,end='')
	flag = 1
	print("\n")
	print(dislist[c],spaces,end='')
	for y in range(len(final_result[x])):
		print(final_result[x][y],spaces*2,end='')
	print("\n")
	c = c+1