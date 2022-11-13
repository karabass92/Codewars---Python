# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    res = s.split()
    l = len(res[0])
    for item in res:
        if len(item) < l:
            l = len(item)
    return l

# =====================================================================

def find_short(s):
    return min([len(item) for item in s.split()])