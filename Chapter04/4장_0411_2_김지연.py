'''
파일 저장 명 : 4장_0411_2_자기이름.py

작성일 : 2023년 4월 11일
학과 : 
학번 :
이름 :
설명 : 점수를 입력 받아 80점 이상이면 "합격"
       아니면 "불합격"을 출력하시오.
       점수와 상관없이 프로그램 마지막에는 "감사합니다"를 출력
'''
# 1. 점수를 입력 받는다.
score = int(input("점수 입력 : "))

# 2. 만약에 점수가 80점 이상이면 :
#   1) "합격입니다."
if score >= 80 :
    print("합격입니다.")

# 3. 아니면
#   1) "불합격입니다."
else :
    print("불합격입니다.")

# 4. 점수와 상관없이 "감사합니다."
print("감사합니다.")