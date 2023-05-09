'''
작성일 : 2023년 5월 9일
학과 : 
학번 :
이름 :
설명 : 입력받은 수가 소수인지 판단하시오.
       
[문제 분석]
소수 :  1을 제외한 자기 자신으로만 나누어 지는 수
입력 받은 수를 2부터 나누어 나머지가 0일 때 판단을 한다.
입력 받은 수와 나누는 수가 같으면 소수이다.
입력 받은 수와 나누는 수가 같지 않으면 소수가 아니다.

입력 받은 수 : input_num
나누는 수 : num
'''
# 1. 정수를 입력 받는다.
# 2. 3부터 입력 받은 수까지 반복하면서
#       1) 만약 수를 입력 받은 수로 나누어 나머지가 0이면
#           ① 멈춘다.
# 3. 만약 입력 받은 수와 나누는 수가 같으면
#       1) 00은 소수입니다.
# 4. 아니면
#       1)00은 소수가 아닙니다.

input_num = int(input("정수 입력 : "))
for num in range(2, input_num+1) :
       if input_num % num == 0 :
              break
if input_num == num :
       print("{}은 소수입니다." .format(input_num))
else :
       print("{}은 소수가 아닙니다." .format(input_num))
       

print("============================")

input_num = int(input("정수 입력 : "))
count = 0
for num in range(2, input_num+1) :
       if input_num % num == 0 :
              count = count + 1
if count == 1 :
       print("{}은 소수입니다." .format(input_num))
else :
       print("{}은 소수가 아닙니다." .format(input_num))