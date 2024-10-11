def printIncreasingPower(x):
    
    number = 1

    while(number * number <= x):

        print (number * number , end = " ")

        number += 1

printIncreasingPower(10)