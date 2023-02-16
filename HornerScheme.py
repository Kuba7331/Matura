
def hornerSchemeRe(factors, rank,x):
    if rank == 0:
        return factors[0]
    else:
        return hornerSchemeRe(factors, rank-1, x) * x + factors[rank]

def hornerSchemeIt(factors, rank, x):
    if rank == 0:
        return factors[0]
    result = factors[0]
    for i in range(rank):
        result = result*x + factors[i + 1]
    return result

factors = [2, 3, 1]
rank = 2
x = 2

print(str(hornerSchemeRe(factors,rank,x)))
print(str(hornerSchemeIt(factors,rank,x)))