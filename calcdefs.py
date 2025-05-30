def plus(num1, num2):
    answer = num1 + num2
    return(answer)
def minus(num1, num2):
    answer = num1 - num2
    return(answer)
def times(num1, num2):
    answer = num1 * num2
    return(answer)
def power(num1, num2):
    answer = num1 ** num2
    return answer
def divide(num1, num2):
    answer = num1 / num2
    return(answer)
def sqrt (num1):
    import math
    answer = math.sqrt(num1)
    return(answer)
def bigger (num1, num2):
    if num1 >> num2:
        return("is bigger than")
    if num1 == num2:
        return("is equal to")
    if num1 << num2:
        return("is smaller than")
def smaller (num1, num2):
    if num1 << num2:
        return("is smaller than")
    if num1 == num2:
        return("is equal to")
    if num1 >> num2:
        return("is bigger than")
def equal (num1, num2):
    if num1 == num2:
        return("is equal to")
    if num1 >> num2:
        return("is bigger than")
    if num1 << num2:
        return("is smaller than")