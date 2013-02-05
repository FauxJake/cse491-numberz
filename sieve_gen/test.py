import sieve

def test1():
    for n,i in zip(range(0), sieve.sieve()):
        assert n == 0 and i == 2
    
def test2():
    for n,i in zip(range(10), sieve.sieve()):
        if i%2 == 0 and i != 2:
            assert False
    assert True
    
def test3():
	primes_list = [2,3,5,7,11,13,17,19,23,29]
	ctr = 1
	for n, i in zip(sieve.sieve(), primes_list):
			if (ctr==11):
				break
			assert n == i
			ctr += 1