'''
저장명 : 3장_연습문제12_이름.py
작성일 : 2023년 4월 4일
학과 : 
학번 :
이름 :
설명 : 윗변, 아랫변, 높이를 입력 받아 
       사다리꼴의 넓이를 구하는 프로그램을 작성하시오.
'''
# 1. 윗변을 입력 받아 정수로 변환하여 변수에 저장
top = int(input('윗변을 입력하시오 : '))

# 2. 아랫변을 입력 받아 정수로 변환하여 변수에 저장
bottom = int(input('아랫변을 입력하시오 : '))

# 3. 높이를 입력 받아 정수로변환하여 변수에 저장
height = int(input('높이를 입력하시오 : '))

# 4. 사다리꼴 넓이를 계산하여 변수에 저장
area = ((top + bottom) * height) / 2

# 5. 사다리꼴 넓이 출력
print("윗변 : ", top, "아랫변 : ", bottom, "높이 : ", height)
print("사다리꼴 넓이는 ", area, "입니다.")

print("윗변 : {}  아랫변 : {}  높이 : {}" .format(top, bottom, height))
print("사다리꼴 넓이는 {:.2f}입니다." .format(area))