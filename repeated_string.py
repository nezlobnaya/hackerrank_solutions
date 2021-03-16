"""
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first letters of the infinite string.
"""

def repeatedString(s, n):
    aCount=0
    aPositions = []
    for i in range(len(s)):
        if s[i] == 'a':
            aCount+=1
            aPositions.append(i)
    div = n//len(s)
    remainder = n%len(s)
    sum = div *aCount
    for i in range(len(aPositions)):
        if aPositions[i] < remainder:
            sum+=1
    return sum