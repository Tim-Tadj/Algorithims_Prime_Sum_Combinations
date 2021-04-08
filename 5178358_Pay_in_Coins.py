import os
import sys
import time

def primeSum(data):
    #initialise varibles 
    sumToReach = data[0]
    lowerExists = False
    upperExists = False
    if len(data) > 1:
        lowerBound = data[1]
        lowerExists = True
    if len(data) > 2:
        upperBound = data[2]
        upperExists = True

    primes = [] #possible primes stored here
    for num in range(1,sumToReach+1):  #find all primes up to the sumToReach
        if num > 1:  
            for i in range(2,num):  #for every number try to see if it can be divided
                if (num % i) == 0:  #break if we find a non-prime number
                    break  
            else:  #execute when for loop doesn't break
                primes.append(num)
    print(primes)
                
    results = []
    


def read_file(Input):
    with open(os.path.join(sys.path[0], Input), "r") as file:
        for line in file:
            stringdata = line.rstrip("\n").split(" ") #create a var for each number
            integer_map = map(int, stringdata) #convert list of strings to map of ints
            data = list(integer_map) #convert map to list
            print(data)
            primeSum(data)


read_file("Input.txt")