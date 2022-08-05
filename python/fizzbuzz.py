def solution0(num):
    if num % 3 == 0:
        return "fizz" 
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz" 
    else:
        return num

def solution1(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz" 
    elif num % 3 == 0:
        return "fizz" 
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

def solution2(num):
    s = ""
    if num % 3 == 0:
        s = "fizz"
    if num % 5 == 0:
        s += "buzz"
    
    return (s or num)

def solution3(num):
    s = "fizz" if num%3==0 else ""
    s += "buzz" if num%5==0 else ""
    return (s or num)


def solution4(num):
    return("fizz"*(num%3==0) + "buzz"*(num%5==0) or num)


for n in range(101):
    print(solution1(n),solution0(n))

    