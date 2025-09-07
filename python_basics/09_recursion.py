# factorial using recursion
def fact(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * fact(n-1)   # recursive case

n = int(input("Enter a number: "))
print(fact(n))  # prints factorial of n


# fibonacci using recursion
def fib(num):
    if num == 0 or num == 1:   # base case
        return num
    return fib(num-1) + fib(num-2)  # recursive case

num = int(input("Enter a number: "))
print(fib(num))  # prints nth fibonacci number
