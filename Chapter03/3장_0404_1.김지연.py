'''
저장명 : 3장_0404_1_이름.py

작성일 : 2023년 4월 4일
학과 : 
학번 :
이름 :
설명 : input() 함수 사용법 익히기.
'''
# 이름을 입력 받아 변수에 저장하시오.
name = input('이름을 입력하시오 : ')

# name 변수에 저장된 이름 출력하시오.
print(name, "님 환영합니다.")
print("{}님 환영합니다." .format(name))

# 국어 점수와 수학 점수를 입력 받으시오.
#                 (입력 받아 변수에 저장)
# score1, score2   /  kor, math
kor = input('국어 점수를 입력 하시오 : ')
math = input('수학 점수를 입력 하시오 : ')

# 두 과목 점수의 합계를 계산하시오.
# 국어와 수학 점수를 합하여 변수에 저장.
total = kor + math

# 합계 출력
print('두 과목 점수의 합계는 ', total, '점 입니다.')
print("두 과목 점수의 합계는 {}점 입니다." .format(total))
# 결과는 문자열 + 문자열로 출력된다.

# 정수를 입력 받기 위해서는 반드시 int() 함수를 사용해야 한다.
# 영어 점수를 입력 받아 정수로 변환하여 변수에 저장하시오.
# 컴퓨터 점수를 입력 받아 정수로 변환하여 변수에 저장하시오.
eng = int(input('영어 점수 입력 : '))
com = int(input('컴퓨터 점수 입력 : '))

# 두 과목의 점수의 합계를 출력하시오.
total = eng + com
print('두 과목 점수의 합계는 ', total, '점 입니다.')
print("두 과목 점수의 합계는 {}점 입니다." .format(total))