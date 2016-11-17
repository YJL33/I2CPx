"""
Inversions
2.0 points possible (graded)
Input file:     inversions.in
Output file:    inversions.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Recall that an inversion in an integer sequence A is a situation when i < j, but Ai > Aj.
Given a sequence of integers. Your task is to count the number of inversions in it.
Hint: to make it faster, you may adapt the mergesort algorithm to solve this problem.

Input

The first line of the input file contains an integer n (1 <= n <= 100000)
- the number of elements in the sequence.
The sequence itself follows in the second line.
All numbers in this sequence do not exceed 10^9 by the absolute value.

Output

Output the number of inversions in the first and only line of the output file.
i n there will be a record i i ai ai, where ai is the i-th element of the initial sequence. 
"""
import sys
import mmap

cnt = 0

def msort(h, lst):          # h: beginning index of list
    # merge sort body
    global cnt
    L = len(lst)
    if L == 1:                          # base case
        return lst
    else:                               # recursive case, pass the original index to merger
        return merger(h, msort(h, lst[:int(L/2)]), msort(h+int(L/2), lst[int(L/2):]))

def merger(s, l, r):
    # merger
    global cnt
    new, curl, curr = [], 0, 0
    while curl < len(l) and curr < len(r):
        if l[curl] <= r[curr]:
            new += l[curl],
            curl += 1
        else:
            # print('+')
            cnt += len(l)-curl          # COUNT INVERSIONS HERE
            new += r[curr],
            curr += 1
    if curl < len(l):
        new += l[curl:]
        # print('+', len(l)-curl)
    if curr < len(r):
        new += r[curr:]
    return new

def writedown(line):
    # writer
    with open('inversions.out', 'w') as output:
        output.write(line)
        output.write('\n')
        # print(line)
        return

with open('inversions.in', 'r') as inputdata:             # read file
    MP = mmap.mmap(inputdata.fileno(), 0, access=mmap.ACCESS_READ)
    N, COUNTER = int(MP.readline()), 0
    ORIGIN = [int(x.decode()) for x in MP.readline()[:-2].split()]
    msort(0, ORIGIN)
    writedown(str(cnt))
    # break