# Advent of code 2018
# Antti "Waitee" Auranen

def main():
    number = 0
    numbers = []
    frequencies = []
    rounds = 0
    while(True):
        try:
            s = int(input('> '))

        except ValueError:
            print("Frequency is " , number)
            break
            
            

        numbers.append(s)
        number += s
        
        for x in frequencies:
            if x == number:
                print("Frequency is " , number)
                print("First frequency twice is ", x)
                return 
        frequencies.append(number)

    while(True):
        rounds += 1
        print("Rounds passed: ", rounds)
        for i in numbers:
            
            number += i
            for x in frequencies:
                if x == number:
                    print("Frequency is " , number)
                    print("First frequency twice is ", x)
                    return 0
            frequencies.append(number)
    return 1

main()