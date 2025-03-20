try:
    num = int(input("Enter your age:"))
    value = 0
    print(num,"!")
    print("Now let's get it divided by 2")
    print("That will give us", num/2)
    print("How about if we divide it by 0?")
    print(num/value)
except ValueError:
    print("That's not an age, Dear!")
except TypeError:
    print("Type with words, not letters.")
except ZeroDivisionError:
    print("Unfortunately we can't divide by 0")