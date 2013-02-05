# an implementation of erosomethingoranother's sieve
# using a python generator, I had some help from the internet with this one
# due to being a bit rusty with python still.

def sieve():
    D = {} #list of primes
    q = 2 #first prime is 2
    
    while True:
        if q not in D: #if q is not in the 
            yield q
            #this is the part i was confused about when I was looking for ero-sieve algorithms,
            #some people were doing D[q*2], and some were doing D[q*q] for the "marking" portion of the algorithm
            #and I don't know what the difference is
            D[q*q] = [q] 
        else:
            #q is not a prime if this is reached
            for p in D[q]:
                D.setdefault(p + q, []).append(p) #marks multiples of the number for later
            del D[q] #removes q from the list
        q+=1 #increments q