import time

# 1. 기본 데코레이터 구조
def deco(func):
    def inner():
        print("running inner")
    return inner

@deco
def target():
    pass

target() # running inner가 출력됨


# 2. 실행 시간 측정 데코레이터 (Clock)
def clock(func):
    def clocked(*args):
        t0 = time.time() # 시작 시간
        
        # 실제 함수(business logic) 수행
        result = func(*args)
        
        elapsed = time.time() - t0 # 소요 시간 계산
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

print('6! = ', factorial(6))
