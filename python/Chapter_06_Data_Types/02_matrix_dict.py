kia = ['김도영', '양현종']
hanhwa = ["류현진", "문동주", "김서현"]
lg = ["문보경", "홍창기", "김현수"]

# 이차원 배열로 작성
baseball = [kia, hanhwa]

# 데이터가 추가되면 출력되는 부분을 수정
baseball.append(lg)

# 데이터를 출력하는 부분
for i in range(len(baseball)):
    if i == 0:
        print("기아:", end = "\t")
    else:
        print("한화:", end = "\t")

    for player in baseball[i]:
        print(player, end = " ")
    print()


kbo = [
    {"team": "기아", "players": kia},
    {"team": "한화", "players": hanhwa},
]

kbo.append({"team": "LG", "players": lg})

for t in kbo:
    print(t["team"], end = "\t")

    for player in t["players"]:
        print(player, end = " ")
    print()
    