#How to use With Keyword
with open('File_Handling/hello.txt','w') as f:
    f.write('Selmon Bhai')
    
#f.write("hello")    


#How to read the file by with keyword
with open('File_Handling/hello.txt','r') as f:
    print(f.read())
    
#To read the character by read function
with open('File_Handling/hello.txt','r') as f:
        print(f.read(2))
        
        
 #To load the big file
big_L = ['hello world'for i in range(1000)]
 
with open('File_Handling/big.txt','w') as f:
    f.writelines(big_L)
    
        
#How to read in chunks
with open('File_Handling/big.txt','r') as f:
    chunk_size=50
    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size),end="****")
        f.read(chunk_size) #To stop the loop (if it will be not there it will become infinte loop)
        
# seek and tell function
with open('File_Handling/hello.txt','r') as f:
        print(f.read(5))
        print(f.tell()) #to check now which charcter wll be procesed
        f.seek(0)
        print(f.read(10 ))
        
#Seek during write
with open('File_Handling/hello.txt','w') as f:
    f.write('Mradul')
    f.seek(0)
    f.write('Xa')        
    
                