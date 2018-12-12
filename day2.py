# Advent of code 2018
# Antti "Waitee" Auranen
# Day 2
def main():
    inputs = []
    checkedinputs = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    doubles = 0
    triples = 0
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    double = False
    triple = False

    inputlength = 26

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

    for i in range(0, len(inputs)):
        
        for j in range(0, len(inputs)) :
            print("i = ", i)
            print("j = ", j)

            for k in range(0, inputlength-1) :
                line1 = inputs[i]
                line2 = inputs[j]
                line1 = line1[:k] + " " + line1[k+1:] 
                line2 = line2[:k] + " " + line2[k+1:] 
                if line1 == line2:
                    print("Line 1: ", inputs[i])
                    print("Line 2: ", inputs[j])
                    print("new   : ", line1)
                    print(" ")
                    
                    checkedinputs.append(line1)
    if len(checkedinputs) > 0:
        
        print("ID found: ", checkedinputs[0])
    else:
        print("ID not found.")
    return 0

main()