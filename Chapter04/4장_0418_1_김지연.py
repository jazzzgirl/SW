'''

'''
# 1. 점수를 입력 받는다.
score = int(input("점수 입력 : "))
# 2. 만약 점수가 0~100 사이 이면
if score >= 0 and score <= 100 : 
    #   1) 만약 점수가 90점 이상이면
    #       ① A학점
    if score >= 90 :
        print("{}점은 A학점입니다." .format(score))
    #   2) 아니고 만약 점수가 80점 이상이면
    #       ① B학점
    elif score >= 80 :
        print("{}점은 B학점입니다." .format(score))
    #   3) 아니고 만약 점수가 70점 이상이면
    #       ① C학점
    elif score >= 70 :
        print("{}점은 C학점입니다." .format(score))
    #   4) 아니고 만약 점수가 60점 이상이면
    #       ① D학점
    elif score >= 60 :
        print("{}점은 D학점입니다." .format(score))
    #   5)  아니면
    #       ① F학점
    else :
        print("{}점은 F학점입니다." .format(score))
# 3. 아니면
#   1)  “잘 못 입력된 점수입니다.”
else :
    print("{}점은 잘못된 점수입니다." .format(score))