from byotest import *

def get_change(amount):
    if amount ==0:
        return []
        
    return [amount]

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])


print("All test passed")