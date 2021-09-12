"""
https://codeforces.com/problemset/problem/580/C
"""

import unittest

test_cases = [
    # (n, m), (cats = 1, no cats = 0), edges, restaurants can visit
    ('4 1', '1 1 0 0', ['1 2', '1 3', '1 4'], 2),
    ('7 1', '1 0 1 1 0 0 0', ['1 2', '1 3', '2 4', '2 5', '3 6', '3 7'], 2),
    ('7 1', '1 1 1 1 0 0 0', ['1 2', '1 3', '2 4', '2 5', '3 6', '3 7'], 0),
    ('5 2', '1 1 0 1 1', ['1 2', '2 3', '3 4', '4 5'], 1),
    ('2 1', '1 1', ['2 1'], 0),
    ('12 3', '1 0 1 0 1 1 1 1 0 0 0 0', ['6 7', '12 1', '9 7', '1 4', '10 7', '7 1', '11 8', '5 1', '3 7', '5 8', '4 2'], 7)
]

'''
12 3
1 0 1 0 1 1 1 1 0 0 0 0
6 7
12 1
9 7
1 4
10 7
7 1
11 8
5 1
3 7
5 8
4 2

should equal 7
'''

def get_tree(n, edges):
    tree = {i: [] for i in range(1, n+1)}  # store the tree in a hash map
    for edge in edges:
        ab = edge.split(' ')
        a, b = int(ab[0]), int(ab[1])
        tree[a].append(b)
        tree[b].append(a)

    return tree


class DFS:
    def __init__(self, tree, cats, m):
        self.ans = 0
        self.tree = tree
        self.cats = cats
        self.m = m

    def search(self, node, cons=0, last_visited=0):
        if self.cats[node-1] == 1:
            cons += 1
        else:
            cons = 0
        if cons > self.m:
            return

        # at leaf
        if len(self.tree[node]) == 1 and node != 1:
            self.ans += 1

        for child in self.tree[node]:
            if child != last_visited:
                self.search(child, cons, node)


def get_restaurants_mem_eff(nm, cats, edges):
    nm = list(map(lambda i: int(i), nm.split(' ')))
    n, m = int(nm[0]), int(nm[1])
    cats = list(map(lambda i: int(i), cats.split(' ')))

    tree = get_tree(n, edges)

    d = [[1, 0, 0]] # node, consecutives, parent_node
    ans = 0
    while d:
        node, cons, parent = d.pop()
        if cats[node-1] == 1:
            cons += 1
        else:
            cons = 0

        if cons > m:
            continue

        if len(tree[node]) == 1 and node != 1:
            ans += 1

        for child in tree[node]:
            if child != parent:
                d.append([child, cons, node])
    return ans

def get_restaurants(nm, cats, edges):
    nm = list(map(lambda i: int(i), nm.split(' ')))
    n, m = int(nm[0]), int(nm[1])
    cats = list(map(lambda i: int(i), cats.split(' ')))

    tree = get_tree(n, edges)
    dfs = DFS(tree, cats, m)
    dfs.search(1)

    return dfs.ans

class TestKefkaAndPark(unittest.TestCase):
    def test_get_restaurants(self):
        for test_case in test_cases:
            res = get_restaurants_mem_eff(
                test_case[0],
                test_case[1],
                test_case[2])
            assert res == test_case[3], f'{test_case}, out = {res}'

if __name__ == '__main__':
    nm = input()
    cats = input()
    n = int(nm.split(' ')[0])
    edges = [input() for i in range(n-1)]

    print(get_restaurants_mem_eff(nm, cats, edges))