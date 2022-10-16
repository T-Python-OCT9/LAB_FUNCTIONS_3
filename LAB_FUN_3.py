start = int(input("enter start number"))
end = int(input("enter the end number"))
for i in range(start,end+1): 
    if i >1:                                                                          #all prime number greater than 1 
        for j in range(2,i):                                                          #check each individual number to see it's prime
            if i%j ==0:                                                               #for every single number
                break                                                                 #we break to go to next number 
        else:
            print(i)
