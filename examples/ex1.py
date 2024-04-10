from heiwa4126.fizzbuzz import fizzbuzz

# from heiwa4126.fizzbuzz import *  ## __all__も書いてあるのでこれでもOK. ただlinterが怒る

print(list(fizzbuzz(10)))
print(tuple(fizzbuzz(15)))
