# Advent of code 2018
# Antti "Waitee" Auranen
# Day 4

# Example of the datetime part of the logs:
# [1518-10-12 00:15]
# 
# Examples of the message part of the logs:
# Guard #1747 begins shift
# falls asleep
# wakes up

def main():

    inputs = []
    guards = []
    while(True):
        s = input("> ")

        #split the lines into tuples for easier sorting
        if len(s) > 0:
            line = (s[1:17], s[19:])
            inputs.append(line)
        else:
            break
    inputs = quickSort(inputs)

    for a in inputs:
        # print(a)
        if a[1][:5] == "Guard":
            guard = a[1][s.find("#")+1 : s.find("begins") -1]
            guards.append([guard, 0])
            
    for a in guards:
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