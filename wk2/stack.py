"""
Stack
2.0 points possible (graded)
Input file:     stack.in
Output file:    stack.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Implement a stack

Input

The first line of the input file contains a single integer number N (1 <= N <= 10^6),
which is the number of commands.
N lines follow, each line contains exactly one command. There are the following commands:

+ x: push x to the stack.
Every x will be an integer such that |x| <= 10^9.
The symbol + and the number will be separated by exactly one white space.
    
-: pop an element from the stack.
It is guaranteed that this operation will never be executed on an empty stack.
There will be at least one such operation.

Output

Output the integers popped from the stack, one per line, in the order they were popped.
"""
# TLE #26
# (hint: io speed)
# 1. directly output the result instead of store the result in memory
# 2. use buffered read/write
# or
# 1. efficiently read the data.
import mmap
with open('stack.in', 'r') as inputdata:
    STK, N = [], int(inputdata.readline())
    with open('stack.out', 'wb') as output:
        # read every line and check whether it's + or -
        MP = mmap.mmap(inputdata.fileno(), 0, access=mmap.ACCESS_READ)
        x = MP.readline()
        while x:
            # a = map(repr, b)
            # print(a, type(a))
            # print(b, type(b), len(b))
            # x = "".join(y for y in b)
            # print(x, type(x), len(x))
            if x == b'-\r\n':
                tmp = STK.pop()
                # print(tmp)
                output.write(tmp)
                # output.write(STK.pop())
                # output.write('\n')
            else:
                STK += x[2:],
            x = MP.readline()
