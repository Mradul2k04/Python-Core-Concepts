import random

num= int(input("Enter thr number of coin flips : "))
if(num<=0):
    print("Invalid number")
flip =num    
head=0
tail=0
while (flip>0):
    toss=random.random()
    if(toss<0.5):
        tail+=1
    else:
        head+=1
    flip -= 1
    
print(f"Head =  {(head/num)*100}")   
print(f"Tail =  {(tail/num)*100}")