#!/usr/bin/env python3

def testPW(pw):
    digits = [int(x) for x in str(pw)]
    double = False
    inc = True
    cn = digits[0]
    for d in digits[1:]:
        if d == cn:
            double = True
        if d < cn:
            inc = False
        cn = d
    return double & inc

def main():
    assert testPW(111111) == True
    assert testPW(223450) == False
    assert testPW(123789) == False

    start = 193651
    end = 649729 + 1
    xcn = 0
    for dd in range(start, end):
        xcn += 1 if testPW(dd) else 0
    print("{} passwords match".format(xcn))

if __name__ == "__main__":
    main()
