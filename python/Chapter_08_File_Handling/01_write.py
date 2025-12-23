try:
    # 파일을 기록할 수 있도록 open
    file = open('./test.txt', 'w')

    # 파일에 한번에 기록
    file.write("Hello Python")
    file.write("\n\n")

    # 줄바꿈이 있는 문자열을 줄 단위로 기록
    msg = "Hello\nPython"
    file.writelines(msg)
    file.write("\n\n")
    file.write(''.join(msg))

except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()