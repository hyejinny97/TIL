# 문제14: 문자의 갯수 구하기
# 문제: 문자열 word가 주어질 때, 해당 문자열에서 `a` 개수를 구하세요. (`count()` 메서드 사용 금지)
# 접근방법
'''
1. for 반복문을 통해 변수 word를 하나씩 읽으면서 'a'인지 확인
2. 'a'가 맞으면 카운트 세기
'''
# 코드
word = 'apple'
cnt = 0
for char in word:
    if char == 'a':
        cnt += 1
print(cnt)



# 문제15: 문자의 위치 구하기
# 문제: 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
'''
a 가 없는 경우에는 -1을 출력해주세요.
find() index() 메서드 사용 금지
'''
# 접근방법
'''
<접근방법1>
 for문과 enumerate()함수를 함께 사용하면 idx와 val값을 동시에 파악해나가면서 쉽게 풀이 가능
<접근방법2>
1. for 반복문을 돌면서 word를 하나씩 읽어나감
2. 글자가 'a'인지 확인하면서, 동시에 인덱스도 하나씩 증가시킴
3. 글자가 'a'가 맞다면, 반복문을 나오고 이때의 인덱스를 출력함
'''
# 코드 1
word = 'banana'
idx = -1
for char in word:
    idx += 1
    if char == 'a':
        break
print(idx)
# 다른 코드 2
word = 'banana'
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break
else:
    print(-1)   # word에 'a'가 없으면 -1을 출력
# 다른 코드 3
word = 'banana'
is_a = False
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        is_a = True
        break
if not is_a:
    print(-1)



# 문제15번 추가문제
# 문제: 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.(find() index() 메서드 사용 금지)
# 접근방법
'''
1. for 반복문을 돌면서 word를 하나씩 읽어나감
2. 글자가 'a'인지 확인하면서, 동시에 인덱스도 하나씩 증가시킴
3. 글자가 'a'가 맞다면, 이때의 인덱스를 따로 변수에 저장
4. for 반복문으로 word를 모두 읽고, 'a'글자가 나올때마다 인덱스를 저장한 후 반복이 끝나면 출력
'''
# 코드 1
word = 'HappyHacking'
rst = ''
idx = -1
for char in word:
    idx += 1
    if char == 'a':
        rst += str(idx)
print(' '.join(rst))
# 코드 2
word = 'HappyHacking'
rst = []
for i in range(len(word)):
    if word[i] == 'a':
        rst.append(str(i))
print(' '.join(rst))
# 코드 3
word = 'HappyHacking'
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')



# 문제16: 모음 등장 여부 확인하기
# 문제: 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
'''
모음 : a, e, i, o, u 
count() 사용 금지
'''
# 접근방법
'''
1. 모음을 리스트 타입의 변수 alph에 담아둔다
2. for 반복문을 통해 word를 한글자씩 읽어가면서, in연산자를 통해 alph에 해당 글자가 있는지 확인
3. 있다면 카운트 세기
'''
# 코드 1 
word = 'apple'
cnt = 0
alph = ['a', 'e', 'i', 'o', 'u']
for char in word:
    if char in alph:
        cnt += 1
print(cnt)
# 코드 2
word = 'apple'
cnt = 0
for char in word:
    if char in 'aeiou':
        cnt += 1
print(cnt)



# 문제17: 소문자-대문자 변환하기
# 문제: 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오. ().upper(), .swapcase() 사용 금지)
# 접근방법
'''
<문제 풀기 전>
 유니코드에서 문자'A'~'Z'를 10진수로 표현했을때 65~90이 됨
 유니코드에서 문자'a'~'z'를 10진수로 표현했을때 97~122가 됨
 ord()함수: 문자 -> 유니코드 숫자로 반환해줌
 chr()함수: 유니코드 숫자 -> 문자로 반환해줌

1. for 반복문을 통해 word를 한글자씩 읽어가기
2. 해당 글자를 ord()함수를 통해 유니코드 숫자로 변환해줌
3. 변환한 값이 97~122 사이이면, 소문자라는 뜻이므로 대문자로 변환해야함
4. 대문자와 소문자의 유니코드 숫자 차이는 32(97 - 65 = 122 - 90 = 32)이므로, ord() 변환값에 32를 빼주면 해당 소문자를 대문자에 해당하는 유니코드 숫자로 바꾸는 것이 됨
5. 대문자에 해당하는 유니코드 숫자를 다시 chr()함수를 통해 문자로 반환해주면 결과적으로 소문자를 대문자로 바꿔줄 수 있음
'''
# 코드
word = 'baNaNa'
rst = ''
for char in word:
    # 소문자이면 대문자로 변환해주기
    if 97 <= ord(char) <= 122:   
        char = ord(char) - 32   # 대문자에 해당하는 유니코드 숫자로 바꿔줌
        rst += chr(char)
    # 대문자이면 변환없이 바로 추가
    else:    
        rst += char
print(rst)



# 문제18: 알파벳 등장 갯수 구하기
# 문제: 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# 접근방법
'''
<접근방법1>
collections를 import해서 Counter()메서드를 사용하면 쉽게 구할 수 있는 문제
<접근방법2>
1. 빈 딕셔너리 타입의 변수 cnt_dict 를 선언
2. for 반복문을 통해 word를 한글자씩 가져오기
3. cnt_dict 변수에 해당 글자가 없으면 값 추가
4. cnt_dict 변수에 해당 글자가 있으면 키를 통해 값에 접근해서 1을 더해주기
'''
# 코드 1
word = 'banana'
# 딕셔너리에 알파벳 갯수를 구해 넣기
cnt_dict = {}
for char in word:
    if char not in cnt_dict:
        cnt_dict[char] = 1
    else:
        cnt_dict[char] += 1
# 알파벳과 갯수 출력
for k in cnt_dict:
    print(k, cnt_dict[k])
# 코드 2
word = 'banana'
cnt_dict = {}
for char in word:
    cnt_dict[char] = cnt_dict.get(char, 0) + 1
# 알파벳과 갯수 출력
for k in cnt_dict:
    print(k, cnt_dict[k])