
nums = [4,2,1,6,9,7]
def square(x):
    return x*x
    
print([square(x) for x in nums])

def is_odd(x):
    return bool(x % 2)
    
# [is_odd(x) for x in nums]

print([x for x in nums if is_odd(x)])


