# an implementation of Eratosthenes' Sieve using
# Python's iterator

class sieve(object):
	def __init__(self):
		self.primeslist = [2]
	
	def __iter__(self):
		return self

	def self.is_prime(n):
		for i in self.primeslist:
			if n % i == 0:
				return False
		return True
		
	def next(self):
		start = self.primeslist[-1] + 1
		while True:
			if sieve.is_prime(self,self.primeslist, start):
				self.primeslist.append(start)
				return start
			start += 1
			