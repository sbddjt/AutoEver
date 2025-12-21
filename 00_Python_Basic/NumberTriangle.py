num = 0 # 출력할 숫자 0 - 9
height = 6 # 삼각형의 높이
row = 0 # 현재 몇 번째 줄

while row < height:
    # 왼쪽 공백 출력
    print(" " * (height - row - 1), end = "")

    # 현재 줄에 필요한 칸의 개수는 2 * row + 1
    for col in range(2 * row + 1):
        # 테두리 조건 체크
        if col == 0 or col == (2 * row) or row == height - 1:
            print(num % 10, end = "")
            num += 1
        else:
            print(" ", end = "")
    
    # 한 줄 다 그렸으니 줄바꿈
    print()
    row += 1