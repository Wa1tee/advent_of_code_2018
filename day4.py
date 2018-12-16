# Advent of code 2018
# Antti "Waitee" Auranen
# Day 4

# [1518-10-12 00:15]
def main():

    inputs = []

    while(True):
        s = input("> ")

        if len(s) > 0:
            line = (s[1:17], s[19:])
            inputs.append(line)
        else:
            break
    inputs = quickSort(inputs)

    for a in inputs:
        print(a)

    return 0



def quickSort(xs):
    before = []
    after = []
    now = []
    
    if len(xs) > 1:
        pivot = xs[0][0]
        for a in xs:
            if a[0] < pivot:
                before.append(a)
            if a[0] == pivot:
                now.append(a)
            if a[0] > pivot:
                after.append(a)
        return quickSort(before) + now + quickSort(after)
    else:
        return xs

main()