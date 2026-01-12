# 🐧 리눅스 쉘(Linux Shell)

## 1. 📝 개요

**정의 및 역할**

- 사용자가 입력한 명령을 해석하여 **커널(Kernel)**로 전달하고, 커널의 처리 결과를 사용자에게 전달하는 **매개체**
- Server의 텍스트 모드(CLI)나 X 윈도(GUI)의 터미널처럼 명령을 입력하는 인터페이스

**주요 기능**

- **🗣️ 명령어 해석기:** 사용자의 명령을 컴퓨터 언어(0, 1)로 변환
- **💻 프로그래밍 (Shell Programming):** 자체 내에 프로그래밍 기능 탑재
    - **Shell Script:** 반복적인 작업을 자동화하기 위해 여러 명령을 묶어 만든 프로그램
- **⚙️ 사용자 환경 설정:** 초기화 파일을 통해 사용자별 맞춤 환경 (PATH, 권한, 변수 등) 제공

---

## 2. 🗂️ 쉘의 종류

| **쉘 이름** | **특징** |
| --- | --- |
| **sh** (Bourne Shell) | 최초의 쉘. 현재는 기능이 미약하여 대부분 bash로 대체됨. |
| **csh** (C Shell) | 2BSD 유닉스 발표. C 언어와 유사한 문법을 가짐. |
| **ksh** (Korn Shell) | AT&T 개발. SVR4 유닉스 발표. sh와 csh의 장점을 결합. |
| **bash** (Bourne Again Shell) | **리눅스 표준(기본) 쉘**. sh와 호환되며 csh, ksh의 편리한 기능 포함. |
| **tcsh** | csh의 기능을 확장하여 개발된 쉘. |
| **dash** | sh 기반. 크기가 매우 작고 가벼워 부팅 스크립트용으로 주로 사용. |
| **zsh** (Z Shell) | bash와 tcsh의 기능 + 강력한 플러그인 및 테마 기능 **(최근 인기)** |

---

## 3. 🔄 Login Shell & Sub Shell

- **Login Shell:** 리눅스에 처음 접속(로그인)했을 때 실행되는 기본 쉘
- **Sub Shell:** 사용자가 프롬프트 상에서 `bash`, `sh` 등을 입력하여 실행한 쉘 (부모-자식 관계 형성)

🚪 **종료 방법 및 차이점**

- **종료 명령:** `Ctrl + d` 또는 `exit`
- **Sub Shell 종료 시:** 이전 쉘(부모 쉘) 환경으로 복귀
- **Login Shell 종료 시:** 터미널이 종료되거나 원격 접속(SSH) 해제

---

## 4. 🐚 Bash Shell 특징

**Ubuntu 등 리눅스 배포판에서 기본 제공**

- **Alias:** 별칭 기능 (긴 명령어를 `alias`로 단축)
- **History:** 사용한 명령어 기록 및 `방향키 ↑` 로 재사용
- **연산 기능:** 쉘 내부에서 산술 연산 가능 (`expr` 등)
- **Job Control:** 백그라운드(`&`), 포그라운드(`fg`) 작업 제어
- **자동 완성:** `Tab` 키를 이용한 명령어/파일명 자동 완성
- **프롬프트 제어 & 명령 편집:** 사용자 편의에 맞게 프롬프트 모양(`PS1`) 변경 가능

---

## 5. ✅ 지원하는 Shell 확인

시스템이 지원하는 쉘 목록은 `/etc/shells` 파일에 저장되어 있습니다.

```bash
cat /etc/shells
```

<img width="748" height="301" alt="Image" src="https://github.com/user-attachments/assets/6c728580-e166-44fe-89a8-a36fbf6075bb" />

---

## 6. ⚙️ Shell 변경

### 1) 현재 사용자의 로그인 쉘 확인

`/etc/passwd` 파일에서 확인 가능합니다.

```bash
# 형식: grep [계정이름] /etc/passwd
grep seongyun /etc/passwd
```

<img width="685" height="47" alt="Image" src="https://github.com/user-attachments/assets/517484f4-8de9-4be7-ace1-463239ede265" />

### 2) 쉘 변경 명령어 (`chsh`)

- **기능: 영구적으로** 로그인 쉘을 변경할 때 사용합니다. **(재로그인 필요)**
- **형식:** `chsh [옵션] [사용자 계정]`

**주요 옵션**

- `-s [절대경로]`: 지정하는 쉘로 변경 (**반드시 절대 경로** 사용)

```bash
# adam 계정의 쉘을 csh로 변경
chsh -s /bin/csh seongyun

# 다시 bash로 복구
chsh -s /bin/bash seongyun
```

<aside>
💡

**절대 경로 vs 상대 경로**

- **절대 경로:** 루트(`/`)부터 시작하는 경로 (불변)
    - 예) `/bin/bash`, `/usr/bin/python`
- **상대 경로:** 현재 위치(`.`)로부터의 경로
    - `./`: 현재 디렉토리 (생략 가능)
    - `../`: 상위 디렉토리
</aside>

- `-l`: 사용 가능한 쉘 목록 출력 (`/etc/shells` 내용)

<aside>
💡

**참고! (Ubuntu)**
우분투(Ubuntu) 환경에서는 **`-l` 옵션이 지원되지 않을 수 있습니다.**
(확인 필요 시 `cat /etc/shells` 명령어를 사용하세요.)

</aside>

**💡 [참고] 일회성 쉘 변경 (Sub Shell)**

```bash
# 쉘 이름 -s sh 사용자 계정 형태
csh -s sh seongyun
```

터미널에서 그냥 `csh` 또는 `sh`를 입력하면 **임시로** 쉘이 바뀝니다.
`exit`를 입력하면 다시 원래 쉘로 돌아옵니다. (설정 유지 안 됨)

---

## 7. 🛠️ 쉘 내장 명령 (Built-in) vs 외부 명령

- **내장 명령**: 쉘 프로그램 자체에 포함된 기능 (`cd`, `echo`, `printf` 등). 별도 파일 없음.
- **외부 명령**: `/bin`, `/usr/bin` 등에 실행 파일로 존재하는 명령 (`ls`, `mkdir` 등).

### 출력 명령

**1) echo**

- 화면에 문자열이나 변수 값 출력

```bash
echo -n "문자열"  # -n: 줄바꿈 안 함
```

**2) printf (C언어 스타일 서식)**

```bash
printf linux              # 줄바꿈 안됨
printf "linux\n"          # 줄바꿈 포함
printf "%d + %d = %d\n" 1 3 4  # 서식 지정 출력
```

<img width="638" height="117" alt="Image" src="https://github.com/user-attachments/assets/fe371db8-7d49-4be1-ac30-dc4a4cd625a2" />

---

## 8. 🔣 특수문자

쉘은 명령 실행 전 특수문자를 먼저 해석(해독)합니다.

### 와일드카드 (Wildcard)

| **기호** | **설명** | **예시 명령어** |
| --- | --- | --- |
| **`*`** | **모든 문자열** (길이 상관없음) | `ls *` (모든 내용 출력)
`cp * /tmp` (전체 복사)
`ls -F t*` (t로 시작하는 모든 것) |
| **`?`** | **문자 한 개** 매칭 | `ls t??` (t로 시작하는 3글자 파일) |
| **`[ ]`** | **대괄호 안의 문자 중 하나** | `ls tmp[135].txt` (tmp1, tmp3, tmp5 찾기) |
| **`-`** | **범위** 지정 | `[a-z]` (소문자)
`[A-Za-z][0-9]` (영문+숫자 조합)
`[가-힣]` (한글) |
| **`[^]`** | **제외** (NOT) | `[^abc]` (a, b, c를 제외한 문자) |
| **`^`** | **줄의 시작** | `^root` (root로 시작하는 줄) |
| **`$`** | **줄의 끝** | `bash$` (bash로 끝나는 줄) |

### 주요 특수문자

- **`~`**: 사용자 홈 디렉토리 (`cd ~`)
- **`-`**: 직전 디렉토리 (`cd -`)

- **`` ` ``(백틱)**: 명령어 실행 결과를 문자열로 대체
    
    ```bash
    echo "Today is date"
    echo "Today is `date`"  # date 명령 실행 결과 출력
    ```
    
    <img width="629" height="92" alt="Image" src="https://github.com/user-attachments/assets/b475170d-29b1-4e8c-9f80-9a42436cb312" />

- **`;` (세미콜론)**: 여러 명령 순차 실행 (앞 명령 실패해도 계속 진행)
- **`&&`**: 앞 명령이 **성공해야만** 다음 명령 수행
    
    ```bash
    cd no_exist_dir; echo "앞에 에러가 났지만 이 문장은 출력됩니다."
    cd no_exist_dir && echo "이 문장은 출력되지 않습니다."
    ```
    
    <img width="760" height="165" alt="Image" src="https://github.com/user-attachments/assets/f278fc40-6972-4b0f-b167-f69e2a63e20e" />
    
- **`|` (파이프)**: 앞 명령의 결과를 뒤 명령의 입력으로 전달 (`ls -al | more`)
- **`\`**: 특수문자 기능 무력화 (문자 그대로 취급)
    
    ```bash
    echo "Price is \$100"
    ```
    
    <img width="743" height="46" alt="Image" src="https://github.com/user-attachments/assets/69e93956-1d96-4c94-a061-7a87fda645e9" />
    

- **`' '` (작은따옴표)**: 모든 특수문자 무력화
- **`" "` (큰따옴표)**: `$`, `\`, ``` 등 일부 기능은 허용
    
    ```bash
    VAR="Hello"
    
    # 1. 작은따옴표 (' '): 보이는 그대로 출력
    echo '$VAR'
    # 출력 결과: $VAR
    
    # 2. 큰따옴표 (" "): 내부의 특수 기능($ 등)을 해석하여 출력
    echo "$VAR"
    # 출력 결과: Hello
    ```
    
    <img width="763" height="94" alt="Image" src="https://github.com/user-attachments/assets/0b4e75d8-941f-4b0d-a621-9c530283bbf1" />
    

---

## 9. 표준 입출력

### 파일 디스크립터

| **번호** | **이름** | **정의** | **기본 장치** |
| --- | --- | --- | --- |
| 0 | **stdin** | 표준 입력 | 키보드 |
| 1 | **stdout** | 표준 출력 | 모니터 |
| 2 | **stderr** | 표준 에러 | 모니터 |

### 1) 출력 리다이렉션 (`>`)

출력의 방향을 변경 (화면 → 파일).

- **`>` (덮어쓰기)**: 기존 내용 삭제 후 저장.
    
    ```bash
    date > date1.txt
    ls -F / > date1.txt  # date 내용 사라짐
    ```
    
- **`>>` (이어쓰기)**: 기존 내용 뒤에 추가.
    
    ```bash
    date >> date1.txt
    ```
    

### 2) 에러 리다이렉션 (`2>`)

에러 메시지를 따로 처리.

```bash
ls abc 2> ls.err       # 에러를 파일에 저장
ls abc 2> /dev/null    # 에러 버리기 (휴지통)
ls abc > ls.out 2>&1   # 표준 출력과 에러를 한 파일에 저장
```

### 3) 입력 리다이렉션 (`<`)

파일의 내용을 명령의 입력으로 사용.

```bash
cat < test.txt
```

---

## 10. 변수

### 1) 변수의 종류

리눅스 변수는 유효 범위에 따라 크게 두 가지로 나뉩니다.

| **구분** | **쉘 변수 (Shell Variable)** | **환경 변수 (Environment Variable)** |
| --- | --- | --- |
| **별칭** | 지역 변수 (Local) | 전역 변수 (Global) |
| **유효 범위** | **현재 로그인한 쉘** 내에서만 유효 | 현재 쉘 + **파생된 자식 프로세스**까지 유효 |
| **사용 예시** | 쉘 스크립트 내부 임시 계산용 | `PATH`, `HOME`, `USER` 등 시스템 설정 |

### 2) 변수 관리 명령어

⚠️ **주의**: 변수를 선언할 때 `=` 앞뒤에 **공백이 있으면 안 됩니다.**

- `A=B` (⭕ 올바른 표현)
- `A = B` (❌ 에러 발생: A라는 명령어를 찾을 수 없음)

| **기능** | **명령어 / 문법** | **예시 코드** | **비고** |
| --- | --- | --- | --- |
| **값 확인** | `echo $변수명` | `echo $PATH` | `$` 기호 필수 |
| **전체 목록** | `env` / `set` | `env` | `env`: 환경 변수만
`set`: 쉘 변수 포함 전체 |
| **쉘 변수 생성** | `변수명=값` | `HYUNDAI=AUTOEVER` | 현재 쉘에서만 유효 |
| **환경 변수 생성** | `export 변수명=값` | `export HYUNDAI=AUTOEVER` | 자식 프로세스로 상속됨 |
| **변수 삭제** | `unset 변수명` | `unset HYUNDAI` | `$` 기호 없음 |

<aside>
💡

`export` 명령은 로그아웃 시 사라집니다.

</aside>

### 3) 변수 영구 저장 (Persistence)

터미널을 재실행해도 변수가 사라지지 않게 하려면 설정 파일에 기록해야 합니다.

- **파일 위치**: `~/.bashrc` (사용자별 설정 파일)
- **등록 방법**:

```bash
# 1. 설정 파일에 export 명령어 추가 (Append)
echo 'export HYUNDAI=AUTOEVER' >> ~/.bashrc

# 2. (선택) vi 편집기로 직접 열어서 수정 가능
# vi ~/.bashrc

# 3. [중요] 변경 사항 즉시 적용 (재로그인 없이)
source ~/.bashrc
```

### 4) 주요 환경 변수

**1.  프롬프트 설정 (`PS1`)**

- **정의 :** 쉘(shell)이 사용자의 명령 입력을 대기하고 있음을 나타내는 표시줄
- **백업 및 커스텀 :**

```bash
PROMPT=$PS1           # 현재 프롬프트 백업
PS1='[\u \T] \!$ '    # 사용자, 시간, 히스토리 번호 등으로 커스텀
PS1=$PROMPT           # 복구
```

<img width="509" height="50" alt="Image" src="https://github.com/user-attachments/assets/09084ec1-e5a9-4df1-9954-d689164eac2b" />

<img width="483" height="59" alt="Image" src="https://github.com/user-attachments/assets/be306267-2373-4d18-8299-779cf9ea388d" />

**2. PATH (가장 중요 ⭐)**

명령어 실행 파일을 찾는 경로들의 모음입니다.

**윈도우와 달리 구분자로 **콜론(`:`)**을 사용합니다.**

**경로 추가 방법**

```bash
# 1. 뒤에 추가 (권장)
PATH="$PATH:~/bin"

# 2. 앞에 추가
PATH="~/bin:$PATH"
```

<aside>
💡

**(강사님 말씀)** PATH 환경변수를 뒤에 추가하는 것이 유지 보수에 편리하므로 권장함.

</aside>

> 🛠️ **안전한 PATH 변경 습관 (백업 및 복구)**
> 
> 
> 환경 변수를 편집할 때는 실수를 대비해 기존 값을 다른 변수에 백업해두는 것이 좋습니다.
> 

```bash
# 1. 기존 PATH 백업
OLDPATH=$PATH

# 2. PATH 변경 시도 (실수 예시: 콜론 대신 세미콜론 사용)
PATH="$PATH;~/bin"
echo $PATH   # 확인: 잘못된 경로가 들어감

# 3. 원상 복구
PATH=$OLDPATH
echo $PATH   # 확인: 원래대로 돌아옴

# 4. 올바르게 다시 수행
PATH="$PATH:~/bin"
echo $PATH   # 성공
```

**Tip**: 프로그램을 압축 해제(`tar/unzip`)하여 설치한 경우, 실행 파일이 있는 디렉토리 전체 경로를 `PATH`에 추가하면 어디서든 명령어로 실행할 수 있습니다.

**3. LANG (로케일 정보)**

- **현재 로케일 확인:** `echo $LANG`

<img width="630" height="42" alt="Image" src="https://github.com/user-attachments/assets/5e5f15c6-12e0-4360-8d81-f0693d6f6394" />

- **지원 로케일 확인:** `locale -a`

<img width="543" height="144" alt="Image" src="https://github.com/user-attachments/assets/8dc8c22b-f7bc-4b2b-9b40-02dc6ceac149" />

- **한국어 패키지 설치 및 설정:**

```bash
sudo apt update
sudo apt install language-pack-ko
sudo locale-gen ko_KR.UTF-8
```

**4. 기타 환경 변수**

| **변수명** | **설명** |
| --- | --- |
| **HOME** | 사용자의 홈 디렉토리 경로 (`~`) |
| **USER** | 현재 로그인한 사용자 아이디 |
| **SHELL** | 현재 사용 중인 쉘의 경로 (예: `/bin/bash`) |
| **PWD** | 현재 작업 중인 디렉토리 (Print Working Directory) |
| **HISTSIZE** | 히스토리(명령어 기록)를 메모리에 저장할 개수 |
| **HISTFILE** | 히스토리가 실제로 저장되는 파일 경로 (`~/.bash_history`) |

---

## 11. 환경 설정 파일

### 개요

시스템을 사용하는 사용자의 환경을 설정하는 파일로 로그인 할 때마다 무조건 실행되는 파일

**1) 시스템 환경 설정 파일 (유저 무관)**

- `/etc/profile`: 모든 shell에 공통으로 적용. 수행 후 `/etc/profile.d/*.sh` 실행
- `/etc/bash.bashrc`: 시스템 공통 bashrc. 기본 프롬프트 및 sudo 힌트 제공
- `/etc/profile.d/*.sh`: 언어나 명령 별로 각각 필요한 환경 제공

2) 사용자 환경 설정 파일 (홈 디렉토리)

로그인 시 시스템 설정 파일 실행 → 이후 사용자 설정 파일 실행 (덮어쓰기)

- `~/.profile`: 경로 추가 등 사용자 정의 환경 설정. 수행 후 `.bashrc` 실행
- `~/.bashrc`: 히스토리 크기, 기본 별명(Alias), 함수 등 설정
- `~/.bash_logout`: 로그아웃할 때 수행할 내용 설정

### 적용 및 관리

환경 설정 파일을 수정하면 로그아웃 후 다시 로그인해야 적용됩니다. 하지만 `source`를 쓰면 즉시 적용 가능합니다.

```bash
source .bash_aliases # 수정한 환경설정 파일을 바로 적용
```

**별명(Alias) 관리 팁**

```bash
alias c=clear        # 현재 shell에서만 적용 (일회성)

vim .bash_aliases    # 별명을 저장할 수 있는 파일 생성/수정
alias c=clear        # 내용 작성 후 저장
source .bash_aliases # 적용
```

---

## 12. bash 옵션

### `set` 명령

- `o`: 옵션 기능 활성화
- `+o`: 옵션 기능 비활성화

**1) ignoreeof**

`Ctrl + D`로 로그아웃되는 것을 방지

```bash
set -o ignoreeof 
# 이제 CTRL + D를 눌러도 로그아웃되지 않음
```

2) noclobber

리다이렉션(`>`)으로 인한 **파일 덮어쓰기 방지**

```bash
touch sample       # 빈 파일 생성
echo $PWD > sample # 출력 방향을 변경해서 내용을 기록
cat sample

set -o noclobber   # 덮어쓰기 방지 기능 활성
echo $PWD > sample # 에러 발생: 파일 수정이 안됨
```
