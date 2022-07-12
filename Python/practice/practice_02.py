'''
# 문제1: 홀수인지 확인하는 조건문 작성
from re import I


num = int(input())
if num % 2 == 1:
    print("홀수")
else:
    print("짝수")

# 문제2: 미세먼지 농도에 따라 등급을 출력하는 조건문 작성
dust = int(input())
if 0 <= dust < 30:
    print("좋음")
elif dust < 80:
    print("보통")
elif dust < 150:
    print("나쁨")
else:
    print("매우 나쁨")

# 문제3: 위 문제 중첩조건문 활용해서 작성
dust = int(input())
if dust < 30:
    if dust < 0:
        print("음수 값입니다.")
    else:
        print("좋음")
elif dust < 80:
    print("보통")
elif dust < 150:
    print("나쁨")
else:
    if dust > 300:
        print("실외 활동을 자제하세요.")
    print("매우 나쁨")

# 문제4: 삼항 연산자
num = int(input())
result = '홀수' if num % 2 == 1 else '짝수'

# 문제5: 1부터 입력한 정수까지의 총합을 구하는 코드 작성
num = int(input())
n = 0
total = 0
while n <= num:
    total += n
    n += 1
print(total)

'''

# 실습1: 수 구분하기
# 문제: 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
# 접근방법:
'''
1. 정수 n이 3의 배수인지 확인하는법: n을 3으로 나눴을 때 나머지가 0이면 3의 배수임
2. 정수 n이 짝수인지 확인하는 법: n을 2로 나눴을 때 나머지가 0이면 짝수임
3. 3의 배수이면서 짝수인지 확인하려면 and연산자를 통해 둘다 True이면 ‘참’을 출력, 하나라도 False이면 ‘거짓’을 출력
'''
# 코드:
n = 126
if n % 3 == 0 and n % 2 == 0:
	print('참')
else:
	print('거짓')



# 실습2: 길이 구하기
# 문제: 문자열 word의 길이를 출력하는 코드를 반복문으로 작성하시오. (len() 함수 사용 금지)
# 접근방법:
'''
1. while문 이용: word의 길이를 카운트해줄 변수 n 생성, 
2. for문 이용(문자열 그대로): for문을 통해 문자열을 하나씩 읽어오면서 변수 n에 카운트
3. for문 이용(index): for문을 통해 인덱스를 하나씩 읽어오면서 변수 n에 카운트
'''
# 코드:
word = 'happy!'
n = 0
for _ in word:
    n += 1
print(n)




# 실습3: 합 구하기
# 문제: 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오. (sum() 함수 사용 금지)
# 접근방법
'''
1. while문 이용: 값을 더해나갈 rst 변수 생성, n부터 1씩 감소시키면서 rst에 값을 더해나감
2. for문 이용: 값을 더해나갈 rst 변수 생성, 1부터 n까지 1씩 증가하면서 rst에 값을 더해나감
'''
# 코드
# 1. while문 이용
n = 10
rst = 0
while n > 0:
    rst += n
    n -= 1
print(rst)
# 2. for문 이용
n = 10
rst = 0
for i in range(1, 10 + 1):
    rst += i
print(rst)



# 실습4: 곱 구하기
# 문제:1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# 접근방법
'''
1. while문 이용: 값을 곱해나갈 rst 변수 생성, n부터 1씩 감소시키면서 rst에 값을 곱해나감
2. for문 이용: 값을 곱해나갈 rst 변수 생성, 1부터 n까지 1씩 증가시키면서 rst에 값을 곱해나감
'''
# 코드
# 1. while문 이용
n = 5
rst = 1
while n > 0:
    rst *= n
    n -= 1
print(rst)
# 2. for문 이용
n = 5
rst = 1
for i in range(1, 5 + 1):
    rst *= i
print(rst)



# 실습5: 평균 구하기
# 문제: 주어진 숫자의 평균을 구하는 코드를 작성하시오. (sum(), len()  함수 사용 금지)
# 접근방법
'''
for 반복문을 돌리면서
1. 숫자의 합을 모두 구한다
2. 숫자의 갯수를 카운트 한다
3. 평균 = 숫자의 합 / 숫자 갯수 을 출력
'''
# 코드
nums = [3, 10, 20]
cnt = 0
sum_nums = 0
for num in nums:
    cnt += 1
    sum_nums += num
print(int(sum_nums / cnt))



# 실습6: 최댓값 구하기
# 문제: 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오. (max() 함수 사용 금지)
# 접근방법
'''
1. 최댓값을 담을 max_num 변수를 매우 작은 값으로 초기화해 이보다 큰 값이 나올때마다 갱신할 수 있도록 함
2. for 반복문을 돌리면서, 요소가 max_num값보다 큰 경우 갱신해줌
'''
# 코드
nums = [0, 20, 100]
max_num = -10**10
for num in nums:
    if max_num < num:
        max_num = num
print(max_num)



# 실습7: 최솟값 구하기
# 문제: 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.(min() 함수 사용 금지)
# 접근방법
'''
1. 최솟값을 담을 min_num 변수를 매우 큰 값으로 초기화해 이보다 작은 값이 나올때마다 갱신할 수 있도록 함
2. for 반복문을 돌리면서, 요소가 min_num값보다 작은 경우 갱신해줌
'''
# 코드
nums = [0, 20, 100]
min_num = 10**10
for num in nums:
    if min_num > num:
        min_num = num
print(min_num)



# 실습8: 두번째로 큰 수 구하기
# 문제: 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.(max() 함수 사용 금지)
# 접근방법
'''
1. 접근방법1: sort()함수를 사용하면 쉽게 구할 수 있는 문제
2. 접근방법2: 가장 큰 수를 구한 후 제거 -> 그다음으로 가장 큰 수를 구하면 두번째로 큰 수를 찾을 수 있음
'''
# 코드
nums = [0, 20, 100]
n = 2
while n > 0:
    max_num = -10**10
    for i in range(0, len(nums)):
        if max_num < nums[i]:
            max_num = nums[i]
    nums.pop(i)
    n -= 1
print(max_num)