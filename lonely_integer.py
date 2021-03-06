# from functools import reduce
# def lonelyinteger(a):
#     ans = reduce((lambda x, y: x^y), a) 
#     return ans

# from collections import Counter
# def lonelyinteger(a):
#     count = dict(Counter(a))
   
#     for k, v in count.items():
#         if v == 1: return k
#     return -1

def lonelyinteger(a):
    hash = {}
    for i in range(len(a)):
        if a[i] not in hash:
            hash[a[i]] = True
        else: hash[a[i]] = False
    for k, v in hash.items():
        if v == True: return k
    return -1