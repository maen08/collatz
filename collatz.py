



def check_even(n):
    series = []
    # n = input('Enter a number:\t')
    for i in range(n, 100000000):
        if n%2 == 0:
            even = (n/2)
            series.append(even)


        else:
            odd = (3*n + 1)
            series.append(odd)

        if n == 1:
            break
        continue
    
   

def series(number):
    number = input('Enter a number:\t')
    for i in range(number, 10000):
        if number%2 == 0:
            check_ever(number)



            
    return 0