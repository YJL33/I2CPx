"""
Win the Competition
2.0 points possible (graded)
Input file:     win.in
Output fole:    win.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Write a program that, given the time Dream Team needs to solve every proposed problem,
can determine what is the maximum possible number of problems they can solve in 300 minutes,
which is the timespan of ACM ICPC World Finals.

Input

The first line of the input file contains an integer number n the number of proposed problems.
(1 <= n <= 15)
The second line contains n integer numbers t1, t2, ..., tn,
where ti is the time, in seconds, which is required to solve the i-th problem.
All ti are positive and don't exceed 10^5.
Please recall that one minute consists of 60 seconds.


Output

Output the single number - the maximum number of problems, which Dream Team can solve.
"""

with open('win.in', 'r') as inputdata:
    N = int(inputdata.readline())
    # 300 minute has 18000 sec.
    RES, i, L, T = 0, 0, 18000, [int(i) for i in inputdata.readline().split(' ')]

T = sorted(T)
# print(T)
while i < N and L-T[i] >= 0:
    RES, L, i = RES+1, L-T[i], i+1

# print(RES)
with open('win.out', 'w') as output:
    output.write(str(RES))
    output.write('\n')
