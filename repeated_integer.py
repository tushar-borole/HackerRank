from collections import defaultdict



def firstDuplicate(a):
    duplicate = defaultdict(int)
    for i in a:
        key = str(i)
        if key in duplicate:
            duplicate[key] += 1
        else:
            duplicate[key] = 0

        if duplicate[key] == 1:
            return key

    return -1

print firstDuplicate([2, 3, 3, 1, 5, 2])