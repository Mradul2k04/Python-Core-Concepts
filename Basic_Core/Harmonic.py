num=int(input("Enter the number : ")) #taking input from user
sum=0 #taking sum variable to do sum 
if(num==0): #check the number is 0 or not
    print("invalid number")
else:
    for i in range(1,num+1): 
        sum=sum+(1/i)
    print(sum)     
