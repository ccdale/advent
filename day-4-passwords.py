#!/usr/bin/env python3

def testPW(pw):
    digits = [int(x) for x in str(pw)]
    double = False
    inc = False
    cn = -1
    for d in digits:
        if d == cn:
            double = True
        if d >= cn:
            inc = True
        cn = d
    return double & inc

def main():
    assert testPW(111111) == True
    assert testPW(223450) == False
    assert testPW(123789) == False

    start = 193651
    end = 649729 + 1
    cn = 0
    for dd in range(start, end):
        cn += 1 if testPW(dd) else 0
    print("{} passwords match")

if __name__ == "__main__":
    main()
