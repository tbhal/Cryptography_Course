# Week 2
# Question 2
# Suppose that using commodity hardware it is possible to
# build a computer for about $200 that can brute force 
# about 1 billion AES keys per second. Suppose an organization
# wants to run an exhaustive search for a single 128-bit AES key 
# and was willing to spend 4 trillion dollars to buy these machines
# (this is more than the annual US federal budget). 
# How long would it take the organization to brute force
# this single 128-bit AES key with these machines?
#  Ignore additional costs such as power and maintenance.

def years():

    price = 200
    budget = 4*pow(10, 12) # 4 trillion
    
    keysPerSecperComputer = pow(10, 9) # 1 billion AES keys per sec
    maxKeys = pow(2,128) # 128 bit AES keys

    numComputers = budget/price
    keysPerSec = keysPerSecperComputer*numComputers

    numSecs = maxKeys/keysPerSec

    print (numSecs , "seconds")
    print(numSecs/3600, "hours")
    print(numSecs/3600/24, "days")
    print(numSecs/3600/24/365, "years")

    hour = 60*60
    day = hour * 24
    week  = day * 7
    month  = day * 31
    year =  day * 365

    print("\n\nMore than an hour but less than a day? ", numSecs > hour and numSecs < day)
    print("More than a day but less than a week? ", numSecs > day and numSecs < week)
    print("More than a week but less than a month? ", numSecs > week and numSecs < month)
    print("More than a 100 years but less than a million years? ", numSecs > 100*year and numSecs < pow(10,6)*year)
    print("More than a billion (10^9) years? ", numSecs > pow(10,9)*year)


years()