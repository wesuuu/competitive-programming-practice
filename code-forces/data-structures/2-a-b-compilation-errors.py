# first line, errors, total n
# n spaced errors
# n - 1 spaced errors subset of 2
# n - 2 all errors from 3 except for 1
# https://codeforces.com/problemset/problem/519/B

i1 = '1 5 8 123 7'
i2 = '123 7 5 1'
i3 = '5 1 7'



def process_input():
    nums = input().split(' ')
    i = [int(i) for i in nums]
    return sorted(i)

def errors(s1, s2):
    for i, num1 in enumerate(s1[0:-1]):
        if s2[i] != num1:
            return num1

    return s1[-1]


_ = input()
s1 = process_input()
s2 = process_input()
s3 = process_input()
print(errors(s1, s2))
print(errors(s2, s3))
