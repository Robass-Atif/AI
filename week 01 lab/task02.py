
def factorial(num):

    # if negative
    if num<0:
      return "Invalid input"  

    if num == 0:
        return 1
    return num*factorial(num - 1)


print(factorial(-1))