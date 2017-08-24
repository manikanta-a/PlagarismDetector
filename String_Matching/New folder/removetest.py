from shutil import copyfile #
import re

file = open('testfile.txt','r')

lst = []

for line in file:
	lst.extend(line.split())

lst2 = []
copyfile('testfile.txt', 'output.txt')


original_string = open('testfile.txt').read()
new_string = re.sub('[^a-zA-Z0-9\n]', ' ', original_string)
open('result.txt', 'w').write(new_string)
file1 = open('result.txt','r')
for line in file1:
	lst2.extend(line.lower().split())

print(file)

print(lst2)