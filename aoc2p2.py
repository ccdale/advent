#!/usr/bin/env python3

import sys

hxv = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]

def runIntcode(vals, xiter=0):
    cn = len(vals)
    icn = 0
    while vals[icn] != 99:
        op = vals[icn]
        v1 = vals[icn+1]
        val1 = vals[v1]
        v2 = vals[icn+2]
        val2 = vals[v2]
        dest = vals[icn+3]
        if op == 1:
            # print("op: {}({}) + {}({}) {} => {}({})".format(v1, val1, v2, val2, val1+val2, dest, vals[dest]))
            vals[dest] = val1 + val2
        elif op == 2:
            # print("op: {}({}) * {}({}) {} => {}({})".format(v1, val1, v2, val2, val1*val2, dest, vals[dest]))
            vals[dest] = val1 * val2
        else:
            print("found op: {}".format(op))
            print("icn: {}".format(icn))
            print("iteration: {}".format(xiter))
            print(vals)
            sys.exit(1)
        icn += 4
        # print("icn: {}".format(icn))
        if icn > cn-1:
            print("out of range")
            break
    return vals[0]

xicn = 0
found = False
for cnv in range(100):
    for cnn in range(100):
        xicn += 1
        xv = []
        for x in hxv:
            xv.append(x)
        xv[1] = cnn
        xv[2] = cnv
        ans = runIntcode(xv, xicn)
        if ans == 19690720:
            print("answer: 19690720, Noun: {}, Verb: {}, iterations: {}".format(cnn, cnv, xicn))
            found = True
            break
    if found:
        break
if not found:
    print("not found")
