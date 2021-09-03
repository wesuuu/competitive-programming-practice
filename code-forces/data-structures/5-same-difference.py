# put value: index into hash O(N)
# iterate over every index and lookup index in hash, if value in hash = array element at index, ++ O(N)

test_cases = int(input())

n = 0
#while n != test_cases - 1:




while n != test_cases:
    pairs = 0

    data = {}
    size = input()
    arr = input().split(' ')
    arr = [int(elem) for elem in arr]
    for i, ai in enumerate(arr):
        diff = ai - i
        try:
            data[diff] += 1
            pairs += data[diff]
        except:
            data[diff] = 0
    print(pairs)
    n += 1