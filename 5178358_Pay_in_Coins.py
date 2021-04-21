import os
import sys
import time
import itertools
def SieveOfEratosthenes(n):
    primes = [1]
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes

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
    
    primes = SieveOfEratosthenes(sumToReach)
    print(primes)
    result = [seq for i in range(len(primes)) for seq in itertools.combinations(primes, i) if sum(seq) == sumToReach]
    print(result)
    input()
    


def read_file(Input):
    with open(os.path.join(sys.path[0], Input), "r") as file:
        for line in file:
            stringdata = line.rstrip("\n").split(" ") #create a var for each number
            integer_map = map(int, stringdata) #convert list of strings to map of ints
            data = list(integer_map) #convert map to list
            # print(data)
            primeSum(data)
            


read_file("Input.txt")