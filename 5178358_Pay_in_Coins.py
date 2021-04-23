import os
import sys
import time
import itertools
import math
import copy

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def SieveOfEratosthenes(number):

    primes = []
    for i in range(2,number+1):
        primes.append(i)

    i = 2
    #from 2 to sqrt(number)
    while(i <= int(math.sqrt(number))):
        #if i is in list
        #then we gotta delete its multiples
        if i in primes:
            #j will give multiples of i,
            #starting from 2*i
            for j in range(i*2, number+1, i):
                if j in primes:
                    #deleting the multiple if found in list
                    primes.remove(j)
        i = i+1

    return (primes)

def sum_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(copy.copy(result))

    for i in range(start, target):
        temp_sum = current_sum + i   
        if not isprime(i):
            continue
        if temp_sum <= target:
            result.append(i)
            sum_rec( target, temp_sum, i, output, result)
            result.pop()
        else:
            return

def sum(target):
    output = []
    result = []
    sum_rec(target, 0, 1, output, result)
    return output

def primesum(data):
    primes = SieveOfEratosthenes(data[0])
    if len(data) == 3:
        pass
    elif len(data) == 2:
        pass
    elif len(data) ==  1:
        return sum(data[0])
    else:
        print("Invalid input file")



def read_file(Input):
    with open(os.path.join(sys.path[0], Input), "r") as file:
        for line in file:
            stringdata = line.rstrip("\n").split(" ") #create a var for each number
            integer_map = map(int, stringdata) #convert list of strings to map of ints
            data = list(integer_map) #convert map to list
            #print(data)
            print(len(primesum(data)))
            

read_file("Input.txt")