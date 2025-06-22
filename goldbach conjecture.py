# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 10:58:49 2025

@author: Vinnie

Goldbach Conjucture (strong): Every even number >2 can be written as the sum of 2 primes

Program Purpose: Identify primes and use them to find examples where this is true.
    Also, if there are any counter examples,the program will identify them
    
Structural Overview:
        Find primes
        Put them in a running list
        Use list to calculate goldbach conjecture
        Update list of numbers that pass the goldbach conjecture
        Iterate up to specified number and notify if conjecture is disproved
        
        
Notes:
    Can test up to 50,000 in 30 seconds
"""
import matplotlib.pyplot as plt
import numpy as np
import time
import math

prime_1 = 0 #first prime number initialized to 0
prime_2 = 0 #second prime number initialized to 0

list_ofprimes = [2] #start list of primes initialized with the first prime (2)

list_ofEvensChecked = [2] #list of even numbers that satisfy goldbachs conjecture initialized to 2

current_number = 3 #initialize the current number being checked against the goldbach conjecture

print(list_ofprimes)



# function:
    # find if number is a prime
# inputs : 
    # number - number to be checked if is prime, 
    # allKnownPrimes - a complete list of all primes less than number
# outputs :
    # new list of all known prime numbers up to and including number
def updateKnownPrimes(number,allKnownPrimes):
    isPrime = 1
    for p in allKnownPrimes:
        if (number % p == 0):
            isPrime = 0
            break
    
    #finished checking all primes
    
    if(isPrime == 1):
        allKnownPrimes.append(number) #prime added to list
        
    return allKnownPrimes


# function:
    # expand list of prime numbers (does not shrink if the refernce number is less than the upper limit)
# inputs : 
    # upperLimit - number up to which you would like to know all prime numbers
    # allKnownPrimes - all known prime numbers (possibly incomplete)
# outputs :
    # new list of all known prime numbers up to and including upperLimit
def expandPrimeList(upperLimit,allKnownPrimes):
    maxPrime = max(allKnownPrimes)
    
    if(upperLimit < maxPrime):
        return allKnownPrimes
    else:
        for num in range(maxPrime+1,upperLimit):
            allKnownPrimes = updateKnownPrimes(num,allKnownPrimes)
        
    return allKnownPrimes

#test cases:
#print(expandPrimeList(30,list_ofprimes))
#print(expandPrimeList(10,list_ofprimes))
#print(expandPrimeList(100,list_ofprimes))


# function:
    # expand list of even numbers that satisfy goldbachs conjecture
# inputs : 
    # upperLimit - number up to which you would like to know all prime numbers
    # allKnownPrimes - all known prime numbers (possibly incomplete)
# outputs :
    # new list of all known prime numbers up to and including upperLimit
def testGoldbachConj(upperLimit,allKnownPrimes,list_ofEvensChecked,print_lists=0):
    
    allKnownPrimes = expandPrimeList(upperLimit,allKnownPrimes) #update 
    if(print_lists == 1):
        print("\nall primes up to ",upperLimit,": \n",allKnownPrimes)
    
    maxGbcEvenChecked = max(list_ofEvensChecked)
   
    startNum = maxGbcEvenChecked+1
    
    upperLimit = max(startNum+1,upperLimit)
    
    for num in range(startNum,upperLimit):
        numSatisfiesGbc = 0
        if(num%2 == 0):
            for p1 in allKnownPrimes:
                if(p1 < num and numSatisfiesGbc==0):
                    for p2 in allKnownPrimes:
                        if(p2 < num):
                            if (p1 + p2 == num):
                                numSatisfiesGbc=1
                                list_ofEvensChecked.append(num)
                                break
                else:
                    break
        else:
            numSatisfiesGbc = 1
            
        
        #print("\nAll numbers that passed goldbach conjectur up to ",upperLimit," are: \n",list_ofEvensChecked)
        if(numSatisfiesGbc==0):
            print("goldbach conjecture disproved!!! The number is ",num)
            break
    if(print_lists==1):
        print("\nAll numbers that passed goldbach conjectur up to ",upperLimit," are: \n",list_ofEvensChecked)
        
    if(numSatisfiesGbc==1):
        print("\nAll numbers passed goldbach conjectur up to ",upperLimit)
            
        

    return list_ofEvensChecked


def plotTimeToComputeGBC(upperLimit,loeChecked,lop):
    
    x = np.logspace(2,math.log10(upperLimit), 10).astype(int)
    #x = np.array([100, 5000, 10000, 25000, 50000, 75000 ,100000,120000,140000,160000,180000, 200000])
    y = np.array([])
    for i in x:
        start_time = time.perf_counter()
        
        loeChecked = testGoldbachConj(i,lop,loeChecked)
        
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        
        y = np.append(y, [elapsed_time])
        

    # Plot the data
    plt.plot(x, y)

    # Add labels and a title
    plt.xlabel("Last Integer To Check")
    plt.ylabel("time (s)")
    plt.title("Time to Compute Goldbach's Conjecture vs Maximum Integer Size")

    # Display the plot
    plt.show()

#main code:
goAgain = 1
while(goAgain == 1):

    badAnswer=1
    
    while(badAnswer == 1):
        print("Please enter the number of (even) integers to check Goldbach's Conjecture against:")
        testLimit = input()
    
        try:
            testLimit = int(testLimit)
            badAnswer = 0
        except ValueError:
            print("Error: Cannot convert string to integer. Try again.\n")
    
        
    print("You entered:", testLimit)
    print("Searching for counter example.....\n")
    
    start_time = time.perf_counter()
    
    list_ofEvensChecked = testGoldbachConj(testLimit,list_ofprimes,list_ofEvensChecked)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds or {elapsed_time/60:.4f} minutes")
    
    badAnswer=1
    while(badAnswer == 1):
        print("Would you like to go again?? ('y' or 'n')\n")
        answer = input()
        if (answer == "y"):
            goAgain = 1
            badAnswer = 0
        elif(answer == "n"):
            goAgain = 0
            badAnswer = 0
        else:
            print("Please enter a valid answer.\n")
          
            
          
            
# Plot Time
plotTimeToComputeGBC(20000,list_ofprimes,list_ofEvensChecked)






