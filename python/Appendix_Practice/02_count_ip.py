# 쿠팡 코딩테스트 문제

try:
    # 파일을 읽어올 수 있도록 open
    file = open("./log.txt")

    loglist = []

    # 줄 단위로 읽어서 loglist에 저장
    for line in file:
        loglist.append(line.strip())
    
    result = {}
    for log in loglist:
        # 9번째를 정수로 변환해서 더해주면 되는데 트래픽이 없을 때 - 라서 정수 변환시 예외가 발생합니다.
        # 예외가 발생하면 아무런 처리를 하지 않던지 0을 더하도록 해주면 됩니다.
        try:
            ip = log.split(" ")[0]
            traffic = int(log.split(" ")[9])
            result[ip] = result.get(ip, 0) + traffic
        except:
            result[ip] = result.get(ip, 0) + 0

    for ip in result:
        print(ip, " : ", result[ip])

except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()