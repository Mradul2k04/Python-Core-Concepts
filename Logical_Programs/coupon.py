import random

num=int(input("Enter a Coupon Number :"))
coupon_num=[]
count=0

while len(coupon_num) <num:
    digit=random.randint(0,num-1)
    count+=1
    if digit not in coupon_num:
        coupon_num.append(digit)
print(f"The number is needed is {count}")        
    