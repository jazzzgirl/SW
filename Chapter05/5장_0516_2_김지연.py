'''
작성일 : 2023년 5월 16일
학과 : 
학번 :
이름 :
설명 : 사용자로부터 가장 좋아하는 월을 입력 받아 
        그 월에 해당되는 계절을 출력하는 프로그램을 
        메뉴 형태로 while 문을 사용하여 작성하시오.
     
=============================
가장 좋아하는 월은?(종료:0)
=============================
****** 5월 ******
5월은 봄에 해당됩니다.


[문제 분석]
월을 입력 받아 저장 : month
0이 입력 될 때까지 반복한다.
3,4,5월은 봄
6,7,8월은 여름
9,10,11월은 가을
12,1,2월은 겨울
나머지는 없는 월이다.
'''
# 1. 무한 반복하면서
#       1) 월을 입력 받는다.
#       2) 비교,판단하여 선택한다.
#           ① 선택에 따른 결과 출력한다.

while True :
    month = int(input("가장 좋아하는 월은?(종료 : 0)"))
    
    # 0 입력을 가장 먼저 체크.
    if month == 0 :
        print("프로그램을 종료합니다.")
        break
    elif month == 3 or month == 4 or month == 5 :
        print("*****", month, "월 *****")
        print(month, "월은 봄에 해당됩니다.")
    elif month == 6 or month == 7 or month == 8 :
        print("*****", month, "월 *****")
        print(month, "월은 여름에 해당됩니다.")
    elif month == 9 or month == 10 or month == 11 :
        print("*****", month, "월 *****")
        print(month, "월은 가을에 해당됩니다.")
    elif month == 12 or month == 1 or month == 2 :
        print("*****", month, "월 *****")
        print(month, "월은 겨울에 해당됩니다.")
    else :
        print("해당 월은 없습니다.")
        
        
while True :
    month = int(input("가장 좋아하는 월은?(종료 : 0)"))
    
    # 0 입력을 가장 먼저 체크.
    if month == 0 :
        print("프로그램을 종료합니다.")
        break
    else :
        if month == 3 or month == 4 or month == 5 :
            print("*****", month, "월 *****")
            print(month, "월은 봄에 해당됩니다.")
        elif month == 6 or month == 7 or month == 8 :
            print("*****", month, "월 *****")
            print(month, "월은 여름에 해당됩니다.")
        elif month == 9 or month == 10 or month == 11 :
            print("*****", month, "월 *****")
            print(month, "월은 가을에 해당됩니다.")
        elif month == 12 or month == 1 or month == 2 :
            print("*****", month, "월 *****")
            print(month, "월은 겨울에 해당됩니다.")
        else :
            print("해당 월은 없습니다.")
        