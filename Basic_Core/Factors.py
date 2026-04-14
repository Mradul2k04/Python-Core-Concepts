num=int(input("Enter the number to find the prime factors : "))
i =2
while(i*i<num):
    while(num%i==0):
        print(f"The prime factor {i}")
        num=num//i
    i+=1    
if(num>1):
    print(f"The prime factor {num}")            
        

