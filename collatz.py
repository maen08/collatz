'''
This function returns a Collatz series and the Number of steps (Total Sequence Order - TSO)

'''


def collatz(num):
    loop = 0
    step = 0
    series = []

    while loop != 1:
        if (num%2 == 0):
            num = int(num/2)
            # print(num)
            series.append(num)

        elif(num%2 != 0):
            num = int(3*num + 1)
            # print(num)
            series.append(num)

        elif(num == 1):
            # print('1')
            series.append('1')

        loop = num
        step += 1
    print('Collatz series:', series)
    print('Number of steps (TSO):', step)

collatz(40)
collatz(42)
