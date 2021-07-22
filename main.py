ings
#two number add together cannot use int to add

#use eval for performance as it is at runtime and not at compile

num1 = '123'
num2 = '456'

def solution(num1,num2):
    #eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))


print(solution(num1,num2))

