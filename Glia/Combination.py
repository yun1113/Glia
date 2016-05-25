'''
Created on 2016年5月25日

@author: CY

C(n,r) = C( n-1, r ) + C(n-1, r-1)
C(n,1) = n
C(n,n) = 1
Compute  C( 990, 33 )
'''
def combination(n, r):
    if r == 1:
        return n
    if r == n:
        return 1
    return combination(n - 1, r) + combination(n - 1, r - 1)

print(combination(5,2))
