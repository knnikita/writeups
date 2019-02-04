#!/usr/bin/python
import os
import string

def run(msg):
    os.system("/root/Desktop/pin3.7/pin -t /root/Desktop/pin3.7/source/tools/ManualExamples/obj-intel64/inscount0.so -- /mnt/hgfs/D/current/dr-owl \"" + "hackim19{" + msg + "\"")
    #print msg
    return int(read("inscount.out").split(" ")[1])


def read(fname):
    with open(fname) as f:
        return f.read()


charset = string.letters + string.digits + " {}=_-!+"
l = []
flag = ""
counter = 0

while len(flag) != 42:
    l = []
    for a in charset:
        count = run((flag + a).ljust(42, "*"))
        l.append((count, a))
    l = sorted(l, reverse=True)
    best = l[0][1]
    flag = flag + best
    print flag
