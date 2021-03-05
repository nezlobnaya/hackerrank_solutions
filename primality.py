def primality(n):
    if n < 2:
        return 'Not prime'
    if n < 3 : return 'Prime'
    if n % 2 == 0: return 'Not prime'

    for i in range(3, round(math.sqrt(n)+1), 2):
        if n % i == 0 : return 'Not prime'
    return 'Prime'
