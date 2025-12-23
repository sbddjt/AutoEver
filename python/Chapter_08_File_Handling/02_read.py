try:
    # 파일을 읽어올 수 있도록 open
    file = open("./test.txt")

    '''# 한 번에 읽기
    msg = file.read()
    print(msg)'''

    # 줄 단위로 읽어서 처리
    for line in file:
        print(line)
        print("-----------")
    
except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()