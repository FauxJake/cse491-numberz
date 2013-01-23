import sieve

def test1():
    for n,i in zip(range(0),sieve.sieve()):
        assert n == 0 and i == 2
    
def test2():
    for n,i in zip(range(10), sieve.sieve()):
        if i%2 == 0 and i != 2:
            assert False
    assert True
    
def test3():
    for n, i in zip(range(10), sieve.sieve()):
        print n,",",i