# 🐧 Shell Script

## 1. Shell Script 개요 ℹ️

### 1) 정의

> UNIX, Linux, Mac OS(POSIX 지원) 등에서 사용하는 명령어들과 if, for 와 같은 프로그래밍적인 요소로 이루어진 **인터프리터 기반의 스크립트 언어**
> 

### 2) 운영체제 환경 (참고) 🖥️

- **UNIX, LINUX :** 기반 OS, CLI(Command Line Interface)로 되어있음. 모바일에서 쓰기 어려움.
- **MAC OS, Android, iOS, Tizen :** GNOME, GUI를 입혀서 사용.
    - *GNOME? 리눅스와 같은 유닉스 계열 운영체제를 위한 데스크톱 환경*

### 3) 셸의 종류 🐚

- **sh :** 셸 스크립트 기반 (Bourne Shell)
- **bash :** 리눅스에서 가장 많이 사용되는 셸. 본 셸(sh)을 기반으로 C 셸과 Korn 셸의 기능을 통합시켜 개량함.
- **ksh :** Korn Shell
- **csh :** C Shell
- **tcsh :** Tenex C Shell
- **zsh :** bash와 ksh, tcsh의 일부 기능을 비롯하여 여러 가지가 개선된 확장된 본 셸

---

## 2. 기본 문법 ✍️

### 1) 생성 및 실행 🏃

**📌 스크립트 만들기**

- 확장자는 `.sh`를 사용합니다.
- 시작할 때는 `#!/bin/bash` (**Shebang**)를 붙여서 해당 파일이 셸 스크립트라는 것을 알려줍니다.
- *이유:* 컴퓨터는 파일 내용만 보고 어떤 shell 문법인지 모르기 때문에 쉬뱅(Shebang)에서 이를 알려줍니다.

**📄 파일 작성 : `shebang.sh`**

```bash
#!/bin/bash

echo "쉬배앵"
```

**🚀 실행 방법**

1. **셸 이름으로 실행** (읽기 권한만 있으면 가능)
- 파일 확인

```bash
seongyun@master:~/shell$ ls -l
total 4
-rw-rw-r-- 1 seongyun seongyun 30 Jan 16 00:20 shebang.sh
```

1. **파일 이름으로 직접 실행**
    - 파일의 소유 권한 변경 (실행 권한 부여)
    - 현재 디렉토리 파일이라도 `PATH`에 없다면 `./`를 붙여야 함.

```bash
chmod 751 shebang.sh
./shebang.sh # 쉬배앵
```

1. **명령어 직접 수행**

```bash
echo "쉬배앵"
```

---

### 2) 변수 사용 📦

**📌 변수 선언**

- `변수명=값` 형태로 선언 (⚠️ **공백 금지**)
- 사용할 때는 `$변수`

```bash
#!/bin/bash

person="기훈이형"
echo "아 shebang $person!!!"

# 결과: 아 shebang 기훈이형!!!
```

> **주의!** 변수 값을 할당할 때 **공백(     )을 주면 명령어로 인식**하여 에러가 발생합니다.
> 

**실행 예시 (디렉토리 생성)**

```bash
#!/bin/bash

language="Korea Newzilang USA"
mkdir $language

# seongyun@master:~/shell$ ls
# Korea  Newzilang  shebang.sh  USA
```

**📌 변수의 종류**

1. **함수 (Function)** 🧩
    - 생성: `function 이름() { 내용 }`
    - 파라미터 사용: `$1`, `$2`... (호출 시 넘겨준 순서대로 대입)
    - 호출: `함수이름 파라미터1 파라미터2...`
    
    ```bash
    #!/bin/bash
    
    function print() {
        echo $1
    }
    
    print "Hello World!" # "Hello World!" 출력
    ```
    

1. **스코프에 따른 분류**
    - **전역 변수:** 함수 외부 선언, 모든 영역 사용 가능
    - **지역 변수:** 함수 내부 선언, 함수 내부에서만 사용 가능
    
2. **환경 변수 (Environment Variable)** 🌍
    - 시스템이 예약해두고 사용하는 변수
    - `HOME`: 사용자 홈 디렉토리
    - `PATH`: 실행 파일을 찾는 경로
    - `PWD`: 현재 작업 중인 디렉토리
    - `USER` / `USERNAME`: 현재 로그인한 사용자 이름
    - `HOSTNAME`: 현재 컴퓨터 이름

**📌 위치 매개변수 (Positional Parameters) 📍**

스크립트 수행 시 함께 넘어오는 파라미터입니다.

- `$0`: 스크립트 이름
- `$1`, `$2` ... `${10}`: 파라미터 순서 (10번째부터는 `{}` 필수)
- `$*`: 전체 인자값 (하나의 문자열로 인식)
- `$@`: 전체 인자값 (`""`로 감싸도 각각 별개로 인식) **★추천**
- `$#`: 매개변수의 총 개수

**위치 매개변수 실습**

```bash
#!/bin/bash

echo "$0"
echo "$1 and $2"
echo "$*"
echo "$@"
echo "$#"
```

- **실행 결과**

```bash
seongyun@master:~/shell$ ./parameter.sh Korea Newziland
# ./parameter.sh
# Korea and Newziland
# Korea Newziland
# Korea Newziland
# 2
```

**📌 특수 매개변수 ✨**

- `$$`: 현재 스크립트/명령어의 PID
- `$?`: **직전 명령의 종료 상태** (0: 성공, 그 외: 에러)

```bash
ls ab
echo $? # 2 (에러 발생)
```

- `$!`: 최근 백그라운드 명령의 PID
- `$-`: 현재 옵션 플래그

---

### 3) 매개변수 확장 (Parameter Expansion) 🚀

**📌 기본 변수 사용**

- 변수명 뒤에 공백 없이 문자열을 붙일 때 `{}` 사용

```bash
AUTH_URL="www.example.com"
echo "https://${AUTH_URL}login.html" 
# https://www.example.comlogin.html 출력
```

📌 **변수 초기화 및 치환**

| **문법** | **변수가 설정 안 됨** | **변수가 NULL(빈 값)임** | **변수에 값이 있음** | **비고** |
| --- | --- | --- | --- | --- |
| **`${var-word}`** | `word` 반환 | 빈 값(`""`) 반환 | 변수값 반환 | 변수 설정 여부만 확인 |
| **`${var:-word}`** | `word` 반환 | **`word` 반환** | 변수값 반환 | **가장 많이 사용 (Null 포함 체크)** |
| **`${var=word}`** | `word`를 **대입** 후 반환 | 빈 값(`""`) 반환 | 변수값 반환 | 변수가 없을 때 실제 값 할당 |
| **`${var:=word}`** | `word`를 **대입** 후 반환 | **`word` 대입 후 반환** | 변수값 반환 | 실무에서 기본값 고정 시 사용 |
| **`${var+word}`** | 빈 값(`""`) 반환 | 빈 값(`""`) 반환 | **`word` 반환** | 변수가 있을 때만 치환 |
| **`${var:+word}`** | 빈 값(`""`) 반환 | 빈 값(`""`) 반환 | `word` 반환 | 변수에 값이 실재할 때만 치환 |
| **`${var?msg}`** | `msg` 출력 후 종료 | 빈 값(`""`) 반환 | 변수값 반환 | 필수 변수 체크 (설정 여부) |
| **`${var:?msg}`** | `msg` 출력 후 종료 | **`msg` 출력 후 종료** | 변수값 반환 | **필수 변수 체크 (Null 방지)** |

**📌 문자열 슬라이싱 (Slicing)**

```bash
OS_TYPE="Redhat Fedora Debian Ubuntu"

echo ${OS_TYPE:14}    # Debian Ubuntu
echo ${OS_TYPE:14:6}  # Debian
echo ${OS_TYPE:(-6)}  # Ubuntu
```

**📌 패턴 제거 및 치환**

- `#`: 앞부분 제거 (짧게) / `##`: 앞부분 제거 (길게)
- `%`: 뒷부분 제거 (짧게) / `%%`: 뒷부분 제거 (길게)
- `/`: 치환 (첫 번째만) / `//`: 치환 (전체)

```bash
FILE_NAME="myvm_container-repo.tar.gz"

# _ 앞부분 모두 제거
echo ${FILE_NAME#*_}   # container-repo.tar.gz

# 마지막 . 앞부분 모두 제거 (확장자 추출)
echo ${FILE_NAME##*.}  # gz

# _ 뒷부분 모두 제거
echo ${FILE_NAME%_*}   # myvm
```

```bash
FILE_PATH="/etc/nova/nova.conf"

# 디렉토리 경로 출력 (뒤에서부터 / 제거)
echo ${FILE_PATH%/*}   # /etc/nova

# 파일 이름만 출력 (앞에서부터 / 제거)
echo ${FILE_PATH##*/}  # nova.conf
```

---

## 3. 제어문 (Control Flow) 🚦

### 1) 조건문 - if, case

**📌 if 문**

`[ ]` 대괄호 안쪽과 연산자 앞뒤에 **반드시 공백**이 있어야 합니다.

```bash
value1=10
value2=20

if [ $value1 -eq $value2 ]; then # 숫자 비교는 -eq 권장
    echo "True"
else
    echo "False"
fi
```

- `z`: 문자열 길이가 0인지 확인

```bash
value=""
if [ -z "$value" ]; then echo "True"; else echo "False"; fi
```

- **클라우드 환경 활용:** 스크립트 내에서 OS를 자동 식별하여 `apt`, `yum` 등 적절한 패키지 매니저를 분기 처리할 때 필수적입니다.

**📌 case 문**

```bash
case $1 in
    start)
        echo "Start" ;;
    restart)
        echo "Restart" ;;
    *)
        echo "Please Sub Command" ;;
esac
```

### 2) 반복문 - for, while 🔄

**📌 for 문**

```bash
# 1. 직접 범위 설정
for num in 1 2 3; do
    echo $num
done

# 2. 파일 목록 (글로빙)
for file in $HOME/*; do
    echo $file
done

# 3. Brace Expansion ({ })
for num in {1..5..2}; do # 1부터 5까지 2씩 증가
    echo $num
done

# 4. 배열 사용
array=("apple" "banana")
for fruit in ${array[@]}; do
    echo $fruit
done

# 5. C 언어 스타일
for ((num=0; num<3; num++)); do
    echo $num
done
```

**📌 while 문**

```bash
num=0
while [ $num -lt 3 ]; do
    echo $num
    num=$((num+1))
done
```

---

## 4. 연산자 (Operators) 🧮

### 1) 비교 연산자

| **종류** | **연산자** | **설명** |
| --- | --- | --- |
| **문자열** | `-z` | 길이가 0이면 참 |
|  | `-n` | 길이가 0이 아니면 참 |
|  | `=`, `==`, `!=` | 같음, 같지 않음 |
| **숫자** | `-eq`, `-ne` | 같음, 같지 않음 |
|  | `-gt`, `-lt` | 큼(`>`), 작음(`<`) |
|  | `-ge`, `-le` | 크거나 같음, 작거나 같음 |
| **논리** | `-a`, `&&` | AND |
|  | `-o`, ` |  |

### 2) 파일/디렉토리 연산자 📂

- `d`: 디렉토리이면 참
- `e`: 존재하면 참 (파일 or 디렉토리)
- `f`: 일반 파일이면 참
- `L`: 심볼릭 링크이면 참
- `r`, `w`, `x`: 읽기/쓰기/실행 권한
- `s`: 파일 크기가 0보다 크면 참
- `nt`, `ot`: 최신 파일/이전 파일 비교

**실습 예제**

```bash
FILE=/etc/localtime
# 심볼릭 링크 확인
if [ -L $FILE ]; then echo True; else echo False; fi # True

FILE=sample.txt
# 내용 존재 여부 확인 (-s)
touch sample.txt
if [ -s $FILE ]; then echo True; else echo False; fi # False (빈 파일)
```

---

## 5. 정규 표현식 (Regular Expression) 🧩

### 1) 개요

리눅스/유닉스에서 검색 효율을 높이기 위해 사용하는 패턴 매칭 방식입니다.

### 2) 메타 문자 (Meta Characters)

- `.`: 한 문자 일치
- : 0번 이상 반복
- `^`: 라인 시작 (`^abc`)
- `$`: 라인 끝 (`xyz$`)
- `[]`: 문자 집합 (`[a-z]`)
- `\`: 특수 문자 이스케이프 (`\?`)

### 3) 문자 클래스 (POSIX)

- `[:alnum:]`: 문자+숫자
- `[:digit:]`: 숫자
- `[:alpha:]`: 알파벳
- `[:space:]`: 공백

### 4) 실습 (grep 활용) 🔍

- 파일 다운로드 및 전송 (`scp` 사용)
- **예제:**

```bash
# C로 시작, U로 끝나는 3글자
grep 'C.U' expression.txt

# q로 시작, 소문자만 존재, ?로 끝남 (확장 정규식 -E 사용 권장)
grep -E 'q[[:lower:]]*\?' expression.txt

# 알파벳 5글자로 시작, 뒤에 : 으로 끝나는 라인
grep -E '^[[:alpha:]]{5}:' expression.txt
```

---

## 6. 스크립트 필수 명령어 🛠️

1. **grep**: 문자열 검색
    - `grep -E "패턴" 파일명`
2. **find**: 파일 검색
    - `find /etc -name "chrony.conf"`
3. **awk**: 데이터 컬럼 추출 (CSV 등 처리에 유용)
4. **sed**: 문자열 치환
    - `sudo sed -i 's/#PermitRoot/PermitRoot/' /etc/ssh/sshd_config` (설정 변경 시 자주 사용)
5. **date**: 날짜 확인
    - `date '+%Y-%m-%d %H:%M'`

---

## 7. 실습: 사용자 계정 자동 생성 스크립트 👤

### 1) 개요

- **목표:** 사용자 ID와 비밀번호 리스트를 받아 계정을 일괄 생성
- **조건:** 인자값 확인, 기존 계정 존재 여부 확인 후 생성

### 2) 스크립트 코드 (`adduser-script.sh`) 💻

```bash
#!/bin/bash

# $1: User ID List (예: "user01 user02")
# $2: Password List (예: "pw01 pw02")

# 1. 인자값 유효성 검사 (두 인자가 모두 존재해야 함)
if [[ -n $1 ]] && [[ -n $2 ]]
then 
  # 배열로 변환
  UserList=($1)
  Password=($2)
  
  # 2. 사용자 리스트만큼 반복
  for (( i=0; i < ${#UserList[@]}; i++))
  do
      # 3. /etc/passwd 에서 계정 존재 여부 확인 (grep -w로 정확한 매칭)
      if [[ $(cat /etc/passwd | grep -w "${UserList[$i]}" | wc -l) == 0 ]]
      then
          # 4. 계정 생성 및 비밀번호 설정 (--stdin 사용)
          sudo useradd ${UserList[$i]}
          echo ${Password[$i]} | sudo passwd ${UserList[$i]} --stdin
          echo "User [${UserList[$i]}] created."
      else
          # 5. 이미 존재하는 경우 메시지 출력
          echo "This user [${UserList[$i]}] is existing"
      fi
  done
else
  # 사용법 안내
  echo -e "Input User ID and Password\nUsage: $0 \"user01 user02\" \"pw01 pw02\""
fi
```

### 3) 실행 방법

```bash
bash adduser-script.sh "dev1 dev2" "pass1 pass2"
```
