'''
Write a python program to read a file line by line and store it into a list.
Your file can contain anything, minimum 10 lines inside the txt file
'''

myFile = open("files.txt",'r')

content = myFile.readlines()
print(content)

myFile.close()