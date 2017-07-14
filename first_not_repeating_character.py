def firstNotRepeatingCharacter(s):
    for i in s:
        if i not in s:
            return i

    return '_'


print firstNotRepeatingCharacter('abacabad')