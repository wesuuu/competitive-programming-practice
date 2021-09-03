# https://codeforces.com/problemset/problem/1324/C

## naive way: check every jump distance starting at 1. If suceed, return first result O(N): worst case multiplied by time to check every value of N

## Binary search: Check half way distance O(log(N)), use greedy algorithm to verify if jump is possible

def check_jump(d, jump_arr):
    start_position = -1
    found_right = False
    left = None
    loops = 0
    while True:
        if start_position + 1 + d > len(jump_arr):
            return True

        for i in range(start_position+1, start_position+d+1):
            j = jump_arr[i]
            if j == 'R':
                start_position = i
                found_right = True
                break
            if j == 'L' and not left:
                left = i
        if left and not found_right:
            start_position = left
        elif not left and not found_right:
            return False
        found_right = False
        left = None
        loops += 1

# def search_d(jump_arr, n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 3

#     if n % 2 == 0:
#         i = int(n / 2)
#     else:
#         i = round(n / 2) - 1
    
#     if check_jump(jump_arr, i):
#         possible_jumps.append(i)
#         return search_d(jump_arr[])
#     else:
#         i =
    
possible_jumps = []

jump_arr = 'RRRR'
jump_arr = list(jump_arr)
print(check_jump(7, jump_arr))

### https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/13/Slides13.pdf