# %%writefile myfile.txt
# Hello this is a text file
# this is the second line
# this is the third line
# myfile =open('myfile.txt')
# print myfile;
# f = open("demofile2.txt","a")
# f.write("Now the file has more content!")
# f.close()

# #f = open("demofile2.txt", "r")

# #print(f.read())

# f = open("demofile2.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# import os
# os.remove("demofile2.txt")


myfile=open("myfile.txt")
print myfile.read()