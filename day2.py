# Advent of code 2018
# Antti "Waitee" Auranen
# Day 2
def main():
    inputs = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    doubles = 0
    triples = 0
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    double = False
    triple = False

    
    while(True):

        s = input('> ')
        if len(s) > 0:
            inputs.append(s)
            amount = 0
            counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for i in s:
                for x in range(0,26):
                    if alphabet[x] == i:
                        counts[x] += 1

            double = False
            triple = False
            # print(counts)
            for j in counts:
                if j == 2:
                    double = True
                if j == 3:
                    triple = True
            if double:
                doubles += 1
                print("Doubleadd: ", doubles)
            if triple:
                triples += 1
                print("Tripleadd: ", triples )
                
        else:
            break

    checksum = doubles * triples
    print("Doubles: ", doubles)
    print("Triples: ", triples)
    print("Checksum is ", checksum)

    return 0

main()