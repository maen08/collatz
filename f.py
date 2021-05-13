
def singleCollatz(num):
    loop = 3
    terms = 0
    while loop != 1:
        if (num % 2 == 0):
            num = int(num/2)
            print(num)
        elif (num % 2 != 0):
            num = int((num * 3) + 1)
            print(num)
        elif (num == 1):
            print("1")
        loop = num
        terms += 1
    print("THE END!")
    print("The total stopping time is " + str(terms))


singleCollatz(7)