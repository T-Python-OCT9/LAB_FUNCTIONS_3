
number2 = int(input("Enter a First number: "))
number3 = int(input("Enter a sec number: "))


def NumberPrime(num : int):
    c=0
    if num > 1:
    
      for n in range(2,num):
        if num % n ==0 :
           c=1
           break
    if c==0:
        print(num)
        
for n in range(number2,number3+1):
    NumberPrime(n)

