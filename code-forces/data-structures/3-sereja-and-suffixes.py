# https://codeforces.com/problemset/problem/368/B


nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])

arr = input().split(' ')

lengths = set()

### O(N)
# iterate over each element in reverse order 
for i in range(n):
    lengths.add(arr[n-i-1]) # add each element to the array
    arr[n-i-1] = len(lengths) # update the array with the length

results = []
for _ in range(m):
    i = int(input())
    print(arr[i-1])
