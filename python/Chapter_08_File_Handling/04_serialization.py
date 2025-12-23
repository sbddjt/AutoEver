import pickle

class VO:
    def __init__ (self, num = 0, name = "nonname"):
        self.num = num
        self.name = name

vo1 = VO(1, "adam")
vo2 = VO(2, "eve")

li = [vo1, vo2]

'''
f = open('./test.txt', 'wb')
pickle.dump(li, f)'''

f = open('./test.txt', 'rb')
result = pickle.load(f)
#print(result)
for r in result:
    print(r.num)