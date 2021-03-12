"""
Given an array of integers and a target value, 
determine the number of pairs of array elements that have a difference equal to the target value. 

"""
def pairs(k, arr):
    aux = set(arr)
    count = 0
    for val in arr:
        target = val + k 
        if target in aux:
            count+=1
    return count

def pairs1(k,arr):
    arr.sort()
    count  = 0
    i,j=0,1
 
    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            count+=1
            j+=1
        elif diff > k: i+=1
        elif diff < k: j+=1
    return count