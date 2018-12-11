# Advent of code 2018
# Antti "Waitee" Auranen

def main():
    number = 0
    while(True):
        try:
            s = int(input('> '))

        except ValueError:
            print("Frequency is " , number)
            return number
        number += s

main()