#!/usr/bin/python3
"""utf8 validation problem   
"""


def validUTF8(data):
    """checks if a list feed to the function are
    valid utf-8 codepoints
    """
    def countOnes(num):
        count = 0
        for i in range(7, -1, -1): # 10000000 = 1 << 7
            if num & (1 << i):
                count += 1
            else:
                break
        return count
    count = 0
    for d in data:
        if not count:
            count = countOnes(d)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
                count -= 1
            else:
                count -= 1
                if countOnes(d) != 1:
                    return False
    return count == 0
