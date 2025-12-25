# 가변 매개변수 (*args)
def tot(*arg):
    result = 0
    for x in arg:
        result = result + x
    return result

print(tot(10, 20))
print(tot(10, 20, 30))
print(tot(10, 20, 30, 40))
