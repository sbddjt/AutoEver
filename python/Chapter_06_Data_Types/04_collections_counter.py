from collections import Counter

'''
# Counter는 데이터의 개수를 셀 때 유용한 클래스
counter = Counter(["red", "blue", "green", "red", "yellow", "blue", "blue"])
print(counter)
print(counter["red"])'''

portfolio = [
    # 이름 수량 가격
    ("apple", 100, 52.5),
    ("google", 50, 91.1),
    ("microsoft", 150, 72.0),
    ("amazon", 200, 83.4),
    ("oracle", 80, 83.4),
    ("apple", 100, 52.5)
]

total_shares = Counter()
#레코드 형태의 데이터의 경우는 무엇을 가지고 개수를 셀 것인지 설정해주면 됩니다.
for name, shares, price in portfolio:
    total_shares[name] = total_shares[name] + 1
print(total_shares)

total_name = Counter()
for name, shares, price in portfolio:
    total_name[name] = total_name[name] + price
print(total_name)


# 상위 3개만 추출
print(total_shares.most_common(3))