import os
import sys
import time
import math
import copy

class Pay_in_coins(): #class to store data for problem
    def __init__(self, datain):
        self.sumto = datain[0] # store the number we are trying to sum to
        if len(datain) == 1:
            self.lower = 1 #stores lower bound for number of sums
            self.upper = self.sumto #stores lower bound for number of sums
        elif len(datain) == 2:
            self.lower = datain[1]
            self.upper = self.lower
        elif len(datain) == 3:
            self.lower = datain[1]
            self.upper = datain[2]
        else:
            print("!:Invalid Input file:!")
        self.rawdata = datain #stores the data input 
        self.primes = self.SieveOfEratosthenes() # creates and stores the primes up to sumto
        self.counter = 0 #stores number of diferent combinations
        self.start_time = 0.0 #stores start time of computation
        self.finish_time = 0.0 #stores finish time of computation

    def printresult(self):
        print("Input:", end =" ")
        for i in self.rawdata:
            print(i, end = " ")
        print("\tOutput:", self.counter, "\tCPU Time(s):", self.finish_time-self.start_time)


    def SieveOfEratosthenes(self):

        primes = []
        for i in range(2,self.sumto+1):
            primes.append(i)

        i = 2
        #from 2 to sqrt(number)
        while(i <= int(math.sqrt(self.sumto))):
            #if i is in list
            #then we gotta delete its multiples
            if i in primes:
                #j will give multiples of i,
                #starting from 2*i
                for j in range(i*2, self.sumto+1, i):
                    if j in primes:
                        #deleting the multiple if found in list
                        primes.remove(j)
            i = i+1
        primes.insert(0, 1)
        return (primes)
    # recursive function to find all combination of prime sums
    def sum_rec(self, current_sum, start, output, result): 
        if current_sum == self.sumto:
            length = len(result)
            if length <= self.upper and length >= self.lower: #append and count solution of it meets requirements
                self.counter +=1
                output.append(copy.copy(result))

        for i in range(start, len(self.primes)):
            temp_sum = current_sum + self.primes[i] #add next prime
            if temp_sum <= self.sumto and len(result) < self.upper: # if we go over our upper bound, stop
                result.append(self.primes[i]) # apply change
                self.sum_rec( temp_sum, i, output, result) # recursivly call itself
                result.pop() # unapply change
            else:
                return

    def primesum(self): #initialise our primesum recursive function
        output = []
        result = []
        self.start_time=time.time() # keep track of execution time
        self.sum_rec(0, 0, output, result) # start solving
        if self.sumto not in self.primes and self.lower == 1: # add gold coin if appliccable
            self.counter +=1
            output.append(self.sumto)
        self.finish_time = time.time() # keep track of execution time
        return output



def read_file(Input):
    with open(Input, "r") as file: #use file in folder of this .py file
        for line in file:  # for every line find a solution
            stringdata = line.rstrip("\n").split(" ") # create a var for each number
            integer_map = map(int, stringdata) # convert list of strings to map of ints
            data = list(integer_map) # convert map to list
            a = Pay_in_coins(data) #initialise
            a.primesum() # solve
            a.printresult() #print results to screen

print(len(sys.argv))
if len(sys.argv) == 2: #if a path is provided use that
    Inputpath = sys.argv[1]
    Input = sys.argv[1]
elif len(sys.argv) == 1: # if a path isn't provided use the file in the same folder as this .py file
    Input = os.path.join(sys.path[0], "Input.txt")

read_file(Input)