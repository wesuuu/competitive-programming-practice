"""
https://codeforces.com/problemset/problem/166/E
1500
"""
import unittest

test_cases = [
    ('2', 3),
    ('4', 21)
]


def get_graph():
    return {
        1: [2,3,4],
        2: [1,3,4],
        3: [1,2,4],
        4: [1,2,3],
    }



def count_cycles(graph, n, node, current_length):
    # quadratic dfs solution, iterate over every possible combination
    cycle_count = 0
    for child in graph[node]:
        if current_length + 1 == n and node == 1:
            continue
        if current_length + 1 == n:
            return 1
        else:
            cycle_count += count_cycles(graph, n, child, current_length + 1)
    return cycle_count

def recurrence(n, node):
    # the recurrence relation, also quadratic if not storing in memory last steps
    if node == 1:
        if n == 0:
            return 1
        return 3 * recurrence(n-1, 0)
    elif node == 0:
        if n == 0:
            return 0
        return 2 * recurrence(n-1, 0) + recurrence(n-1, 1)

def recurrence_count(n):
    # O(N) solution, store previous counts in matrix
    dp = [[0]*(n+1), [0]*(n+1)]
    dp[1][0] = 1
    dp[0][0] = 0
    j = 1
    while j <= n:
        dp[1][j] = 3*dp[0][j-1] % ((10**9) + 7)
        dp[0][j] = 2*dp[0][j-1] + dp[1][j-1] % ((10**9) + 7)
        j += 1

    return dp[1][n] 

class TestTetrahedron(unittest.TestCase):
    def test_count_cycles(self):
        for test_case in test_cases:
            assert recurrence_count(int(test_case[0])) == int(test_case[1])

if __name__ == '__main__':
    n = int(input())
    print(recurrence_count(n))