# https://codeforces.com/problemset/problem/466/C

n = int(input())

# 1. check that the sum S of array is divisible by 3, if not, return 0
# 2. 

arr = input().split(' ')
arr = [int(elem) for elem in arr]

S = sum(arr)

if S % 3 != 0:
    print(0)
else:
    s3 = S / 3
    i = 0
    j = 0
    current_sum = 0
    for k, elem in enumerate(arr[:-1]):
        current_sum += elem

        if current_sum == s3 * 2:
            j += i
        if current_sum == s3:
            i += 1


    print(j)
    
'''
9
0 0 0 0 0 0 0 0 0

= 28
'''