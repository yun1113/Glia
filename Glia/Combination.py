'''
Created on 2016年5月25日

@author: CY

C(n,r) = C( n-1, r ) + C(n-1, r-1)
C(n,1) = n
C(n,n) = 1
Compute  C( 990, 33 )
'''

# VERY SLOW ...
# def combination(n, r):
#     if r == 1:
#         return n
#     if r == n:
#         return 1
#     return combination(n - 1, r) + combination(n - 1, r - 1)
# 
# print(combination(990,33))

 
import time
 
combDict = {}
 
def combination(n, r):
    if (n, r) in combDict.keys():
        return combDict[(n, r)]
     
    if r == 1:
        return n
    if r == n:
        return 1
     
    combDict[(n - 1, r)] = combination(n - 1, r)
    combDict[(n - 1, r - 1)] = combination(n - 1, r - 1)
     
    return  combDict[(n - 1, r)] + combDict[(n - 1, r - 1)] 
 
# tStart = time.time()
# print(combination(5, 2))
print(combination(990,33))
# tEnd = time.time()
# print("cost: ", tStart - tEnd)
