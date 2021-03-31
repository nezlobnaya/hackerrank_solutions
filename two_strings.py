def twoStrings(s1, s2):
    aux = set(s2)

    for char in s1:
        if char in aux: return 'YES' 
    return 'NO'