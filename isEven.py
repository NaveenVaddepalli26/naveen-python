# Write a function to find given number is even or not

'''n = int(input("Enter a number:"))

def isEven(num):
    if num%2==0:
        return True
    return False

print("Given number is ",isEven(n))'''

n = int(input("Enter a range:"))

def isEven(num):
    if num%2==0:
        return True
    return False

#print("Given number is ",isEven(n))
count = 0
for i in range(2,n+1):
     if isEven(i):
         print(i,end=' ')
         count += 1
print("Evens in between",n,"is" ,count)
 
