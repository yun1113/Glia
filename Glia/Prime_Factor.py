'''
Created on 2016年5月25日

@author: user


The largest prime factors.
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import math

def check_prime(num):
    for i in range(math.floor(math.sqrt(num))+1):
        if i <= 1:
            continue
        mod = num % i
        if mod == 0:
            return False  # not prime
    return True      

NUMBER = 600851475143
# NUMBER = 13195
up = math.floor(math.sqrt(NUMBER))
# print(up)

prime_list = []
for i in range(up):
    if i <= 1:
        continue
    check = check_prime(i)
    if check:
#       print("Prime:", i)
        mod = NUMBER % i
        if mod == 0:
            prime_list.append(i)

print(prime_list.pop()) # 6857

  
            

