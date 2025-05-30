import calcdefs
import find_common
def calc():
    print("-------------newline------------")
    print("hello! welcome to boaz's calculator app")
    do = input("what do you want to do(+, -, *, /, >, <, =, find most common, sqrt or power)")
    allowed = ["+", "*", "/", "-", "power", ">", "<", "="]
    if do in allowed:
        num1 = float(input("first number"))
        num2 = float(input("second number"))
        if do == "+":
            print(f"{num1} plus {num2} is {calcdefs.plus(num1,num2)}")
        else:
            if do == "-":
                print(f"{num1} minus {num2} is {calcdefs.minus(num1,num2)}")
            else:
                if do == "*":
                    print(f"{num1} times {num2} is {calcdefs.times(num1,num2)}")
                else:
                    if do == "/":
                        print(f"{num1} divided by {num2} is {calcdefs.divide(num1,num2)}")
                    else:
                       if do == "power":
                           print(f"{num1} to the power of {num2} is {calcdefs.power(num1,num2)}")
                       else:
                         if do == ">":
                            print(f"{num1} {calcdefs.bigger(num1, num2)} {num2}")
                         else:
                                if do == "<":
                                   print(f"{num1} {calcdefs.smaller(num1, num2)} {num2}")
                                else:
                                  if do == "=":
                                        print(f"{num1} {calcdefs.equal(num1, num2)} {num2}")
    else:
       if do == "sqrt":
         num3 = input("what number do you want to square root")
         print(f"the square root of {num3} is {calcdefs.sqrt(num3)}")
       if do == "find most common":
          find_common.most_common()
calc()
