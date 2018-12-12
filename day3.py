# Advent of code 2018
# Antti "Waitee" Auranen
# Day 3

def main():

    row = []
    matrix = []
    overlap = 0
    claims = []
    idnumbers = []
    for x in range(1,1200):
        row = []
        for y in range(1,1200):
            row.append(0)
        matrix.append(row)

    for x in range(1,1200):
        row = []
        for y in range(1,1200):
            row.append(0)
        claims.append(row)

    while(True):
        s = input("> ")

        if len(s) > 0:
            
            idno    = int( s[ 1 : s.find("@") - 1 ])
            left    = int( s[ s.find("@")  + 1 : s.find(",") ])
            top     = int( s[ s.find(",")  + 1 : s.find(":") ])
            width   = int( s[ s.find(": ") + 2 : s.find("x") ])
            height  = int( s[ s.find("x")  + 1 : ])

            idnumbers.append(idno)
            
            for i in range(left, left + width):
                for j in range(top, top + height):
                    matrix[j][i] += 1
                    if claims[j][i] > 0:
                        idnumbers[claims[j][i]-1] = 0
                        idnumbers[idno -1] = 0
                    claims[j][i] = idno

        else:
            break

    for i in matrix:
        for j in i:
            if j > 1:
                overlap += 1
    for i in idnumbers:
        if i > 0:
            print("Non-overlapping claim: ", i)
    print("Overlapping square inches: ", overlap)

    return 0


main()