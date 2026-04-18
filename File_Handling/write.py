f = open("File_Handling/hello.txt","w") #To create the file if it is  not present
f.write("Learning python") #To Write Something in the file
f.close()

# Since the file is closed the write operation will not work
#f.write("mradul")

# To add multiple Lines
f=open("File_Handling/Sample.txt","w")
f.write("Hello")
f.write("\nMy self Mradul Sharma")
f.close()


# If we have to write on the file that is already present

f=open("File_Handling/hello.txt","w")
f.write("I am the coder")
f.close()

#To write the something on the present file wihout removing the file
f=open("File_Handling/Sample.txt","a")
f.write("\n I am Fine")
f.close()

#Write multiple Lines
l=['Hello\n','How\n','Do\n','Yon\n','Learned\n','Python']
f=open("File_Handling/hello.txt","w")
f.writelines(l)
f.close()
 


