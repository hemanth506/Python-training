
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def prime(num):
    get_prime = []
    for n in range(2,num):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            get_prime.append(n)
    print(get_prime)

a = [236,487]
