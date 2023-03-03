"""
작성일 : 2021년 5월 21일
작성자 : 학과 학번 이름
설명 : 구구단 출력하기 - 결과가 짝수인 것 만 출력하기
"""

for dan in range(2, 10) :
    print('::', dan, '단::')
    for su in range(1,10) :
        if (dan % 2 == 0) or (su % 2 == 0) : 
            print(dan, 'x', su, '=', dan*su)