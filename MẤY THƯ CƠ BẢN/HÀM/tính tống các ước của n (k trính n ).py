n = int(input())

def sumOfAll(n):
    Sum = 1
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            Sum += i
            if i != n/i:
                Sum += n/i
    return int(Sum)
print(sumOfAll(n))