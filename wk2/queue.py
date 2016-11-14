"""
Queue
2.0 points possible (graded)
Input file:     queue.in
Output file:    queue.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Implement a queue

Input

The first line of the input file contains a single integer number N (1 <= N <= 10^6),
which is the number of commands.
N lines follow, each line contains exactly one command. There are the following commands:

+ x: push x to the queue.
Every x will be an integer such that |x| <= 10^9.
The symbol + and the number will be separated by exactly one white space.
    
-: pop an element from the queue.
It is guaranteed that this operation will never be executed on an empty queue.
There will be at least one such operation.

Output

Output the integers popped from the queue, one per line, in the order they were popped.
"""
# modified from stack.py
import mmap
from collections import deque
with open('queue.in', 'r') as inputdata:
    QUEUE, N = deque(), int(inputdata.readline())
    with open('queue.out', 'wb') as output:
        # read every line and check whether it's + or -
        MP = mmap.mmap(inputdata.fileno(), 0, access=mmap.ACCESS_READ)
        y = MP.readline()
        x = MP.readline()
        while x:
            # a = map(repr, b)
            # print(a, type(a))
            # print(b, type(b), len(b))
            # x = "".join(y for y in b)
            # print(x, type(x), len(x))
            if x == b'-\r\n':
                tmp = QUEUE.popleft()
                # print(tmp)
                output.write(tmp)
                # output.write(QUEUE.pop())
                # output.write('\n')
            else:
                QUEUE += x[2:],
            x = MP.readline()
