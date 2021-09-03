def is_anagram(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)

    if s1_set == s2_set:
        return True
    return False

def sort_string(s):
    x = sorted(s)
    return ''.join(x)
    

def sherlockAndAnagrams(s):
    # Write your code here
    # iterate over every character
    # store character in a set
    # as move, store all possible substrings in same set
    # iterate over each item in the set
    
    # construct substrings
    substrings = {i: [] for i in range(len(s))} # O(N)
    sub = ''
    anagram_pairs = 0 
    for i, char in enumerate(s): # O(N)
        substrings[0].append(char)
        sub = sub + char

        if i != 0:
            
            substrings[i].append(sort_string(sub))
            n = len(sub)
            j = 1
            while j != n - 1:
                tmp = sub[j:len(sub)]
                if tmp != '':
                    substrings[n-j-1].append(sort_string(tmp))
                j += 1

    indexes  = {i: [] for i in range(len(s))}
    for a, chars in substrings.items():
        i = 0
        for j, char in enumerate(chars):
            while i != len(chars):
                if char == chars[i] and j != i:
                    index_pair = set([i,j])
                    if index_pair not in indexes[a]:
                        anagram_pairs += 1
                        indexes[a].append(index_pair)
                i += 1
            i = 0
    return anagram_pairs

import math

def sherlockAndAnagrams(s):
    # Write your code here
    # iterate over every character
    # store character in a set
    # as move, store all possible substrings in same set
    # iterate over each item in the set
    n = len(s)
    pairs = 1
    existing_pairs = []
    anagrams = 0
    if n == 1:
        return 1
    j = n
    while pairs != n:

        for i in range(0, j):
            s_pair = s[i:i+pairs]
            for p in existing_pairs:
                if is_anagram(p, s_pair):
                    print(i)
                    anagrams += 1
            existing_pairs.append(s_pair)
        pairs += 1
        j -= 1
    print(existing_pairs)
    return anagrams
        
    
s = 'kkkk'
#s = 'abba'

print(sherlockAndAnagrams(s))