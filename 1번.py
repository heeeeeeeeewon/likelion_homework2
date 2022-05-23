#1

x, y = map(int, input("연산을 진행할 두 숫자를 입력하시오").split())

def plus(a,b):
    return a+b

def sub(a,b):
    return a-b

def trip(a,b):
    return a*b

def slic(a,b):
    return a//b

def nama(a,b):
    return a%b

num = input("어떠한 연산을 수행할까요?")

if num == '+':
    print(x,"+",y,"=",plus(x,y))
elif num == '-':
    print(x,"+",y,"=",sub(x,y))
elif num == '*':
    print(x,"+",y,"=",trip(x,y))
elif num == '/':
    print(x,"+",y,"=",slic(x,y))
elif num == '%':
    print(x,"+",y,"=",nama(x,y))
else:
    print("해당 연산은 지원하지 않습니다.")

#while문은 어떻게 적용해야할지 모르겠습니당 ... 