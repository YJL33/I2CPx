"""
Queue with Minimum
2.0 points possible (graded)
Input file:     queuemin.in
Output file:    queuemin.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Implement a queue which supports push and pop operations,
and additionally a minimum query, which returns a minimum among the elements in the queue.
For every minimum query, output its result.

Input

The first line of the input file contains a single integer number N (1 <= N <= 10^6)
- the number of commands.
N lines follow, each line contains exactly one command.

There are the following commands:

+ x: push x to the queue. Every x will be an integer such that |x| <= 10^9.
The symbol + and the number will be separated by exactly one white space.
−: pop an element from the queue.
It is guaranteed that this operation will never be executed on an empty queue.
?: query a minimum element in the queue.
It is guaranteed that this operation will never be executed on an empty queue.
There will be at least one such query.

Output

Output the results of the minimum queries on the queue,
one per line, in the order they were performed.
"""
# modified from stack.py
import mmap
from collections import deque
import heapq

with open('queuemin.in', 'r') as inputdata:
    QUEUE, MINHP, N = deque(), [], int(inputdata.readline())
    NEG = {}
    with open('queuemin.out', 'wb') as output:
        # read every line and check whether it's + or -
        MP = mmap.mmap(inputdata.fileno(), 0, access=mmap.ACCESS_READ)
        y = MP.readline()
        x = MP.readline()
        while x:
            # print(x, type(x), len(x))
            if x == b'-\r\n':
                tmp = QUEUE.popleft()
                if tmp == MINHP[0][1]:
                    heapq.heappop(MINHP)
                else:
                    if tmp in NEG:
                        NEG[tmp] += 1
                    else:
                        NEG[tmp] = 1
            elif x == b'?\r\n':
                tmp2 = MINHP[0][1]
                while tmp2 in NEG and NEG[tmp2] > 0:
                    NEG[tmp2] -= 1
                    heapq.heappop(MINHP)
                    tmp2 = MINHP[0][1]
                # print("peek ", MINHP[0][0])
                output.write(tmp2)

            else:
                QUEUE += x[2:],
                heapq.heappush(MINHP, (int(x[2:]), x[2:]))       # use a tuple for heap sorting.
            x = MP.readline()
            # print("NOW: ", QUEUE)
            # print("NOW: ", MINHP)
# 