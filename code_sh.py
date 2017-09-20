#!/Users/erikjensen/Documents/miniconda3/envs/idp/bin/python

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("           TESTING PYTHON              ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import fileinput

print ("Text to search for:")
textToSearch = input( "> " ) 

print ("Text to replace it with:")
textToReplace = input( "> " )

print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )

with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, textToReplace), end='')


# mainfile = open('main.cpp','r+') #r+ is a read/append mode, r for read, w for write (erases previous file of same name)

# for line in mainfile:
# 	print line, # the comma seems to remove the extra space
# #mainfile.write("Hello Silly") #Appends the string to the EOF
# mainfile.close()

# #Same code as above (minus the write())
# with open('main.cpp') as mainfile2:
# 	for line in mainfile2:
# 		print line,

# with open('main.cpp') as mainfile3:
# 	data = mainfile3.readlines()
# 	for line in data:
# 		words = line.split()
# 		print words


# readFile = open('main.cpp','r')
# writeFile = open('main2.cpp','w')

# lines = readFile.readlines()
# for line in lines:
# 	words = line.split()
# 	if words == '//IFDEF':

