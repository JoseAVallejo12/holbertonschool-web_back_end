#!/usr/bin/env python3
import math
add = __import__('0-add').add
floor = __import__('2-floor').floor
to_kv = __import__('7-to_kv').to_kv
to_str = __import__('3-to_str').to_str
a = __import__('4-define_variables').a
concat = __import__('1-concat').concat
pi = __import__('4-define_variables').pi
sum_list = __import__('5-sum_list').sum_list
school = __import__('4-define_variables').school
sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list
element_length =  __import__('9-element_length').element_length
i_understand_annotations = __import__('4-define_variables').i_understand_annotations


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

print('======= # Test task 3 ==========')
pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))


print('======= # Test task 4 ==========')
print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))


print('======= # Test task 5 ==========')
floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))


print('======= # Test task 6 ==========')
print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))


print('======= # Test task 7 ==========')
print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

print('======= # Test task 8 ==========')
make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))

print('======= # Test task 9 ==========')
print(element_length.__annotations__)