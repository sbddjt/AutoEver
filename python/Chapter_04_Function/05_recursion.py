# 1. 피보나치 수열 (반복문)
def fibonacci_loop(n:int) -> int:
    result = 1
    first = 1
    second = 1
    for _ in range(3, n+1):
        result = first + second
        second = first
        first = result
    return result

print(f"Loop(10): {fibonacci_loop(10)}")
print(f"Loop(30): {fibonacci_loop(30)}")


# 2. 피보나치 수열 (재귀)
def fibonacci_recursive(n:int) -> int:
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

print(f"Recursive(10): {fibonacci_recursive(10)}")
# print(fibonacci_recursive(100)) # Stack Overflow 주의
