# 프린트 함수
print('kdt')

# 점심 메뉴가 담긴 리스트를 만들고 첫번째 메뉴 출력하기
lunch_menu = ['rice', 'seaweed', 'kimchi']
print(lunch_menu[0])

# codeup 6009 문제: input을 받아서 출력
text = input('문자를 입력:')
print(text)

# 입력받은 숫자에 5를 더한 결과를 출력하기
num = int(input('숫자 입력:'))   # 주의) 명시적 형변환하자!
print(num + 5)

# split()함수: 문자열을 특정 단위로 쪼개줌
a = '1 2 3'
rst = a.split()
print(rst)

a = '10:20'
rst = a.split(':')
print(rst)
print(rst[0], rst[1], sep='^')