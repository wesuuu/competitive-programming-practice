"""
https://codeforces.com/problemset/problem/1336/A
1600

FIXME when time
"""
import unittest
import heapq, collections
test_cases = [
    ('7 4', ['1 2', '1 3', '1 4', '3 5', '3 6', '4 7'], 7),
    ('4 1', ['1 2', '1 3', '2 4'], 2),
    ('8 5', ['7 5', '1 7', '6 1', '3 7', '8 3', '2 1', '4 5'], 9),
    ('20 7', ['9 7', '3 7', '15 9', '1 3', '11 9', '18 7', '17 18', '20 1', '4 11', '2 11', '12 18', '8 18', '13 2', '19 2', '10 9', '6 13', '5 8', '14 1', '16 13'], 38)
]


def get_tree(edges):
    defaultree = collections.defaultdict(list)

    for edge in edges:
        a, b = tuple(map(int, edge.split(' ')))
        defaultree[a].append(b)
        defaultree[b].append(a)
    return defaultree


def dfs(tree, visits, queue, node=1, current_dist=0):
    subtree_size = 1
    for child in tree[node]:
        if child != node and not visits[child]:
            visits[child] = True
            subtree_size += dfs(tree, visits, queue, child, current_dist+1)
    queue = heapq.heappush(queue, (-1*(current_dist - subtree_size), node, current_dist))
    return subtree_size

def max_happiness(edges, k):
    tree = get_tree(edges)
    visits = {i+1: False for i in range(len(tree.keys()))}
    visits[1] = True
    queue = []
    res = dfs(tree, visits, queue)

    i = 0
    total = 0
    print(queue)
    while i != k:
        item = heapq.heappop(queue)
        total += item[-1]
        i += 1
        print(item, total)
    return total


class TestLinovaAndKingdom(unittest.TestCase):
    def test_max_happiness(self):
        for test_case in test_cases:
            nk, edges, solution = test_case
            n, k = tuple(map(int, nk.split(' ')))
            ans = max_happiness(edges, k)
            assert ans == solution, f'{test_case}, {ans}'

if __name__ == '__main__':
    n, k = tuple(map(int, input().split(' ')))
    print(n, k)
    edges = [input() for i in range(n-1)]
    print(max_happiness(edges, k))