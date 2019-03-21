# Date: 2019-03-20

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import sys

arr = list(map(lambda x: int(x), sys.argv[1].split(',')))
equal_pairs = [(a, b) for i, a in enumerate(arr) for j, b in enumerate(arr[i+1:]) if a + b == int(sys.argv[2])]

print(equal_pairs)
