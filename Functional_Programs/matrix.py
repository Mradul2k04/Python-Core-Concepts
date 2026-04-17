m=int(input("Enter the number of rows : "))
n=int(input("Enter thr number of columns : "))

arr=[]
print(f"Enter {m*n} Elements")
for i in range(m):
    rows=[]
    for j in range(n):
        num=int(input("Enter the numbers : "))
        rows.append(num)
    arr.append(rows)
print("2D array output")
for i in range(m):
    for i in range(n):
        print(arr[i][j],end=" ")
    print()            
        
    
