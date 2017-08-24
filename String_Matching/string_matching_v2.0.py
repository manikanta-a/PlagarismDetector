import string
from shutil import copyfile 
import re
import os
import math


class LCS(object):
	def __init__(self):
		pass
		#self.file1 = file1
		#self.file2 = file2

	def length_of_file(self,file):
		self.file = file
		f = open(self.file)
		length = len(f.read())
		return length

	def comparision(self,file1,file2):
		self.file1 = file1
		self.file2 = file2
		lst1 = self.words_to_list(self.file1)
		lst2 = self.words_to_list(self.file2)
		self.length = len(lst1)-1 + len(lst2)-1
		# self.length2 = len(lst2)-1
		#lcs = 0
		maxi = 0
		for x in range(len(lst1)):
			y = 0
			while(y<len(lst2)):
				tempx = x
				lcs=0
				if (lst1[tempx]==lst2[y]):
					while(tempx<len(lst1) and y<len(lst2)  and lst1[tempx] == lst2[y]):
						lcs = lcs + len(lst2[y])
						tempx = tempx + 1
						y = y + 1
				else:
					y = y+1
			
				if lcs > maxi:
					maxi = lcs
				
		res = (maxi*2)/(self.length_of_file(self.file1)+self.length_of_file(self.file2))
		#print(res)
		return round(res*100,2)


	def words_to_list(self,file):
		self.file = file
		lst = []
		original_string = open(self.file).read()
		new_string = re.sub('[^a-zA-Z0-9\n]', ' ', original_string)
		open('temp.txt', 'w').write(new_string)
		file1 = open(self.file,'r')
		for line in file1:
			lst.extend(line.lower().split())

		return lst

	def lcs_all(self,path):
		self.path = path
		self.pathlist = [p for p in os.listdir(self.path) if p.endswith('.txt') and p != "temp.txt"]
		os.chdir(self.path)
		matrix2 = []

		for i in range(len(self.pathlist)):
			matrix = []
			for j in range(len(self.pathlist)):
				if i == j:
					per = 100.00
				else:
					per = self.comparision(self.pathlist[i],self.pathlist[j])
				matrix.append(per)
			matrix2.append(matrix)

		return matrix2


objLCS = LCS()

user_input = input("Enter the path : ")

mat = objLCS.lcs_all(user_input)

listoffiles = [p for p in os.listdir(user_input) if p.endswith('.txt') and p != "temp.txt"]
#print(pathlist)
length = len(listoffiles)

dislist = []

print("This is String Matching Algorithm ")

for i in range(1,length+1):
	dislist = dislist + ["file"+str(i)]

print("\n")
for i in range(length):
	
	print(dislist[i]," = ", listoffiles[i])


spaces = '     '
flag = 0
c = 0

print("\n")
for x in mat:
	if flag == 0:
		print('   ',spaces*2,end='')
		for g in dislist:
			print(g,spaces*2,end='')
	flag = 1
	print("\n")
	print(dislist[c],spaces,end='')	
	for y in x:
		print(y,spaces*2,end='')
	print("\n")
	c = c+1
#print(mat)

