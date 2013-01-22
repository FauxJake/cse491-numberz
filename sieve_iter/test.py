import sieve

def test1():
    f = sieve.sieve()
    i = iter(f)
    assert i.next() == 3
    
def test2():
    f = sieve.sieve()
    i = iter(f)
    i.next()
    assert i.next() == 5
    
def test3():
    f = sieve.sieve()
    i = iter(f)
    i.next()
    i.next()
    assert i.next() == 7
    
test1()
test2()
test3()