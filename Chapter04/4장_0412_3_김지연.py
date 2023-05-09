'''
파일 저장 명 : 4장_0412_3_자기이름.py

작성일 : 2023년 4월 12일
학과 : 
학번 :
이름 :
설명 : 점수를 입력 받아 학점을 출력하시오.
'''
score = int(input("점수를 입력 하시오 : "))

print("=== 조건식1 ===")
if 90 <= score <= 100 :
    print("A")
elif 80 <= score <= 89 :
    print("B")
elif 70 <= score <= 79 :
    print("C")
elif 60 <= score <= 69 :
    print("D")
else :
    print("F")

print("=== 조건식2 ===")    
if 90 <= score <= 100 :
    print("A")
elif 80 <= score < 90 :
    print("B")
elif 70 <= score < 80 :
    print("C")
elif 60 <= score < 70 :
    print("D")
else :
    print("F")
    
print("=== 조건식3 ===")
if (score >= 90) and (score <= 100) :
    print("A")
elif (score >= 80) and (score <= 89) :
    print("B")
elif (score >= 70) and (score <= 79) :
    print("C")
elif (score >= 60) and (score <= 69) :
    print("D")
elif (score >= 0) and (score <= 59) :
    print("F")
else :
    print("잘못 입력")
    
print("=== 조건식4 ===")
if score > 100 :
    print("잘못 입력 ")
elif score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
elif score > 0 :
    print("F")
else :
    print("잘못 입력 ")
    
print("=== 조건식5 ===")
if 90 <= score <= 100 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")