def test_always_pass():
    assert True
    
def test_always_fail():
    assert(False)
    
def test_capitalize():
    assert("daniel".capitalize() == "Daniel")
    
def test_reversed():
    assert(list(reversed([1,2,3,4]))==[4,3,2,1])
    
def test_some_primes():
    assert 37 in {
        num for num in range(1,50)
        if num !=1 and not any([num%div ==0 for div in range(2,num)])
    }