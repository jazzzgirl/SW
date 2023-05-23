'''
작성일 : 2023년 5월 16일
학과 : 
학번 :
이름 :
설명 : 10개의 정수를 입력 받아 
        합을 구하는 프로그램을 작성하시오.
        단, 짝수 번째에 입력되는 숫자는 
        양수를 음수로, 음수는 양수로 바꾸어 합을 구하시오.
     
[문제 분석]
입력 받는 수 : num
10번 반복 : count
양수 → 음수 : num * -1
음수 → 양수 : num * -1

짝수번 째 입력 값인지 판단하여 
양수는 음수로, 음수는 양수로 바꾼다.

반복하면서 판단하여 선택한다.
'''
# 1. count = 1, sum = 0 초기화
# 2. count가 10까지 반복하면서
#       1) 정수를 입력 받는다.
#       2) 만약 count 가 짝수이면(짝수번째)
#           ① 양수를 음수로, 음수를 양수로 바꾼다.
#       3) 합계를 계산한다.
#       4) count를 1 증가한다.
# 3. 합계를 출력한다.

count = 1
sum = 0
while count <= 10 : 
    num = int(input(str(count) + "번째 정수 입력 : "))
    if count % 2 == 0 :
        num = num * -1
    sum = sum + num
    count = count + 1
print("10개 정수의 합 : ", sum)

print("----------------------------------")

count = 1
sum = 0
while True :
    num = int(input("{}번째 정수 입력 : " .format(count)))
    if count % 2 == 0 :
        num = -num
    sum += num
    count += 1
    
    if count > 10 :
        break
print("10개 정수의 합 : {}" .format(sum))
