#!/usr/bin/env python3
import math
concat = __import__('1-concat').concat
add = __import__('0-add').add
floor = __import__('2-floor').floor


print('======= # Test task 0 ==========')
print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)


print('======= # Test task 1 ==========')
str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

print('======= # Test task 2 ==========')
ans = floor(3.14)
ans2 = floor(666.666)

print(ans == math.floor(3.14))
print(ans2 == math.floor(666.666))

print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))