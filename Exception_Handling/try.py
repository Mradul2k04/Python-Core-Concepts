# let create a file
with open("Exception_Handling/Sample.txt","w") as f:
    f.write("hello world")
    
    
    
#now use try and except in this if file is not present
try:
    with open("Exception_Handling/Sample1.txt","r") as f:
        print(f.read())
except:
    print("file not found")            
    
    
#catch specific exception
try:
  m=5
  f = open('Exception_Handling/Sample.txt','r')
  print(f.read())
  print(m)
  print(5/2)
  L = [1,2,3]
  L[100]
except FileNotFoundError:
  print('file not found')
except NameError:
  print('variable not defined')
except ZeroDivisionError:
  print("can't divide by 0")
except Exception as e:
  print(e)
  
  
# else
try:
  f = open('Exception_Handling/Sample.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else:
  print(f.read())
  
  
# finally
# else
try:
  f = open('Exception_Handling/Sample.txt','r')
except FileNotFoundError:
  print('file nai mili')
except Exception:
  print('kuch to lafda hai')
else:
  print(f.read())
finally:
  print('ye to print hoga hi')  
  
  
  

  
  
  
  
    
    