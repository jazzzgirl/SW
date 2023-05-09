age = int(input("나이 입력 : "))
height = int(input("키 입력 : "))

print(":: 내포된 if문 ::")
if age >= 8 :   # 8세 이상인가?
    if height >= 120 :  # 키가 120 이상인가?
        print("고속")
    else :      # 아닌가?
        print("저속")
else :  # 아닌가?
    print("입장 불가")
    
print("---------------------")    

print(":: 다중 if문 ::")
if age >= 8 and height >= 120 : # 8세 이상이고, 키가 120 이상인가?
    print("고속")
elif age >= 8 and height < 120 :    # 8세 이상이고, 키가 120 미만인가?
    print("저속")
else :      # 아닌가?
    print("입장 불가")