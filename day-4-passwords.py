#!/usr/bin/env python3

import sys

def findGroups(digits):
    cn = digits[0]
    groups = {}
    delete = []
    for d in digits[1:]:
        if d == cn:
            if d not in groups:
                groups[d] = 2
            else:
                groups[d] += 1
        cn = d
    for group in groups:
        if groups[group] % 2 == 0:
            delete.append(group)
    for d in delete:
        del(groups[d])
    return groups

def testPW(pw):
    digits = [int(x) for x in str(pw)]
    grps = findGroups(digits)
    if len(grps) > 0:
        print(pw, grps)
        return False
    double = False
    inc = True
    cn = digits[0]
    for d in digits[1:]:
        if d == cn:
            double = True
        if d < cn:
            inc = False
            break
        cn = d
    return double & inc

def main():
    assert testPW(111111) == True
    assert testPW(223450) == False
    assert testPW(123789) == False
    assert testPW(112233) == True
    assert testPW(123444) == False
    assert testPW(111122) == True
    assert testPW(112221) == False
    assert testPW(112222) == True

    start = 193651
    end = 649729 + 1
    xcn = 0
    for dd in range(start, end):
        xcn += 1 if testPW(dd) else 0
    print("{} passwords match".format(xcn))

if __name__ == "__main__":
    main()
