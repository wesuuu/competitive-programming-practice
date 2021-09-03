def twoStrings(s1, s2):
    # Write your code here
    d1 = {s: True for s in list(s1)} # O(N)
    is_subset = False

    for s in list(s2): # at most, O(N)
        try:
            d1[s]
            is_subset = True
            break
        except:
            pass

    return is_subset

s1 = 'hello'
s2 = 'world'

print(twoStrings(s1, s2))

s1 = 'hi'
print(twoStrings(s1, s2))