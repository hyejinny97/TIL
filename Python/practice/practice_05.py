# 예제03: [오류 해결] 입력 받기
# 문제: 두 수를 Input으로 받아 합을 구하는 코드이다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
numbers = input().split()
print(sum(numbers))
'''
# 오류 원인
'''
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
# 오류 분석
'''
1. input()함수의 반환값은 문자열 타입
2. sum()함수에서 인자는 숫자형 타입으로 묶여진 iterable객체를 받아야함
3. 결국 문자열을 합할 수는 없으므로 에러가 발생함
'''
# 오류 해결
numbers = map(int, input().split())
print(sum(numbers))





# 예제04: [오류 해결] 입력 받기2
# 문제: 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
words = list(map(int, input().split()))
print(words)
'''
# 오류 원인
'''
ValueError: invalid literal for int() with base 10: 'i'
'''
# 오류 분석
'''
1. int()함수의 인자로는 숫자형 데이터타입이 들어가야한다. 
2. 결국 input()함수의 반환값인 문자열이 int()함수의 인자로 들어갔으므로 에러가 발생했다.
3. 문자열을 입력받아 단어별로 나누려면, split()함수만 써도 충분하다.
'''
# 오류 해결
words = input().split()
print(words)





# 예제05: [오류 해결] 숫자의 길이 구하기
# 문제: 아래 코드는 숫자의 길이를 구하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
number = 22020718
print(len(number))
'''
# 오류 원인
'''
TypeError: object of type 'int' has no len()
'''
# 오류 분석
'''
len()함수는 인자로 숫자형 데이터 타입을 받지 않는다.
따라서, str()으로 타입변환 후 다시 len()함수를 이용해 숫자의 길이를 출력해보자.
'''
# 오류 해결
number = 22020718
print(len(str(number)))





# 예제06: [오류 해결] 1부터 N까지의 2의 곱 저장하기
# 문제: 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
'''
# 오류 원인
'''
AttributeError: 'tuple' object has no attribute 'append'
'''
# 오류 분석
'''
튜플 데이터 타입은 append()메서드를 지원하지 않는다.
튜플 대신 리스트를 이용해서 값을 담아보자.
'''
# 오류 해결
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)





# 예제07: [오류 해결] 평균 구하기
# 문제: 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)
'''
# 오류 원인
'''
  File "<stdin>", line 3      
    count += 1
    ^
SyntaxError: invalid syntax  
'''
# 오류 분석
'''
1. 들여쓰기를 하지 않아서 발생한 에러이다.
    => for문 안에서 카운트를 세게끔 변경해주자.
2. 평균을 구해서 결과를 출력하고자 할때, 보통 몫의 값만 나타내는 것이 아니라 실수형으로 나타내므로 코드 일부를 수정하고자 한다.
'''
# 오류 해결
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)





# 예제08: [오류 해결] 모음의 개수 찾기
# 문제: 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)
'''
# 오류 분석
'''
if문의 코드를 해석해보자면, char라는 변수가 'a'인지의 여부에 따라 T/F를 반환해 주고 그 이후에 'e','i','o','u'는 True로 처리된다. 
or 연산자는 하나만 True여도 전체가 True이니까 char에 어떤 값이 할당이 되든 항상 if 조건문은 True가 되므로 모든 알파벳이 카운트되어 12를 출력하게 된다.
'''
# 오류 해결
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)





# 예제09: [오류 해결] 과일 개수 구하기
# 문제: 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
'''
# 오류 분석
'''
fruit_count 딕셔너리 변수에 값을 추가하고자 할때에는, fruit_count[fruit] = 1의 방식으로 추가해야 한다. 
'''
# 오류 해결
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)





# 예제10: [오류 해결] 더 큰 최댓값 찾기
# 문제: 아래 코드는 리스트에서 최댓값을 구하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
'''
# 오류 원인
'''
오류 1)
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

오류 2)
  File "<stdin>", line 1, in <module>
NameError: name 'max2' is not defined
'''
# 오류 분석
'''
1. 파이썬 내장 함수 중 max라는 이름의 함수가 존재하는데, 위 두번째줄 코드를 보면 max라는 변수에 max()함수의 반환값을 할당되었으므로 max는 숫자형 데이터 타입의 변수로 변환된 것과 다름없다.
2. 따라서 위 네번째줄 코드에서 max라는 숫자형 데이터 타입 변수룰 함수처럼 사용하려고 하니까 에러가 난 것이다.(오류1) 물론 이로 인해 결국 변수 max2는 어떠한 값도 할당받지 못했다.(오류2)
'''
# 오류 해결
number_list1 = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list1)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")





# 예제11: [오류 해결] 영화 정보 찾기
# 문제: 아래 코드는 영화의 장르id를 장르 이름으로 바꿔서 영화 정보를 출력하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
'''
from pprint import pprint

def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }


if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))
'''
# 오류 분석
'''
movie_info()함수에서 반환값이 없으니까 print()를 통해 출력하려고해도 어떠한 값도 출력되지 않는다.
'''
# 오류 해결
from pprint import pprint

def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }
    return new_movie_info


if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))





# 문제19: 숫자의 길이 구하기
# 문제: 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. (양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지)
# 접근 방법
'''
첫째자릿수부터 자릿수를 높여나가면서 10의 지수을 나눈 후, 몫이 존재하면 해당 자릿수까지 수가 존재함을 의미
'''
# 코드 1
number = 123
n = 1
while True:
    if number // 10 ** n:
        n += 1
        continue
    break
print(n)
# 코드 2
number = 123
cnt = 0
while number:
    number //= 10
    cnt += 1
print(cnt)
# 코드 3
import math
number = 123
print(int(math.log10(number)) + 1)