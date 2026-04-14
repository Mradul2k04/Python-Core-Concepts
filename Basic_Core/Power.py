num=int(input("Enter a number : "))
if 0<num<31:
    for i in range(num+1):
        print(2**i)
else:
    print("overflow")        
