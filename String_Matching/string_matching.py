import string
import math
from shutil import copyfile #
import re


class EliminatingSpecialChars(object):
	pass

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
		print(res)
		return maxi


	def words_to_list(self,file):
		self.file = file
		lst = []
		read = open(self.file,'r')
		for line in read:
			lst.extend(line.lower().split())

		return lst

testLCS = LCS()
lst = testLCS.comparision("text1.txt","text2.txt")

print(lst)

