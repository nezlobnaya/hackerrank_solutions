

# Complete the reverseArray function below.
def reverseArray(a):
    # return a[::-1]
    # return [a[len(a) -1 -i] for i in range(len(a))]
    aux= []
    for i in range(len(a)):
      aux.append(a[len(a) - 1- i])
    return aux
    

