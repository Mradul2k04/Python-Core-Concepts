#How to read the file which is present
f=open("File_Handling/Sample.txt","r")
s=f.read()
print(s)
f.close()

#Can Read the character how many you have to read
f=open("File_Handling/Sample.txt","r")
s=f.read(10)
print(s)
f.close()

#Read line by line
f=open("File_Handling/Sample.txt","r")
print(f.readline(),end='')
print(f.readline(),end='')
f.close()


#read the entire using readline
f=open("File_Handling/Sample.txt","r")
while True:
    data=f.readline()
    
    if data=="":
        break
    else:
        print(data,end='')
f.close()
