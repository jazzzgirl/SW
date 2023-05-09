'''
숫자 > 연산자 > 숫자 입력 받기
'''
num1 = int(input("첫 번 째 수 입력 : "))
cal = int(input("연산자 입력 : "))
num2 = int(input("두 번 째 수 입력 : "))

if cal == '+' :
    print("{} + {} = {}" .format(num1, num2, num1+num2))
elif cal == '-' :
    print("{} - {} = {}" .format(num1, num2, num1-num2))
elif cal == '*' :
    print("{} * {} = {}" .format(num1, num2, num1*num2))
elif cal == '/' :
    print("{} / {} = {}" .format(num1, num2, num1/num2))
else :
    print("해당 연산자 ")