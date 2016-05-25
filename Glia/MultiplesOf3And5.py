'''
Created on 2016年5月25日

@author: CY

Multiples of 3 and 5. 
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23
Please find the sum of all the multiples of 3 or 5 below 1000.
'''

three = {item for item in range(1,1000) if item % 3 == 0}
five = {item for item in range(1,1000) if item % 5 == 0}
# print(three)
# print(five)
three_five = three | five
# print(three_five)

sum = 0
for i in three_five:
    sum += i
print(sum)