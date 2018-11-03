def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr:
        if len(aStr) > 1:
            test = aStr[len(aStr) // 2]
            if char > test:
                return isIn(char, aStr[aStr.index(test) + 1:])
            elif char < test:
                return isIn(char, aStr[:aStr.index(test)])
            else:
                return char == test
        else:
            return char == aStr
    else:
        return False

if __name__ == "__main__":
    print(isIn('d', ''))