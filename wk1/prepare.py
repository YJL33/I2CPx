"""
Prepare Yourself to Competitions!
2.0 points possible (graded)
Input file:     prepare.in
Output file:    prepare.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Input

The first line of the input file contains an integer n (2 <= n <= 100).
The second line contains n integers p1, p2 , ... , pn , separated by whitespace.
The third line contains n integers t1, t2, ..., tn, separated by whitespace.

All pi and ti are positive and do not exceed 1000.

Output

Output the maximum possible value of ability to solve problems, which Jamie can achieve in n days.
Pay attention to the fact that Jamie should spend at least one day for each theory and practicing.

Examples
prepare.in  prepare.out
2
1 2
2 1
            4
3
1 2 3
1 2 3       6
"""
with open('prepare.in', 'r') as inputdata:
    N = int(inputdata.readline())
    T = [int(x) for x in inputdata.readline().split(' ')]
    P = [int(x) for x in inputdata.readline().split(' ')]

# mindiff is the minimum difference between ti and pi
# in case all chosen from one array.
RES, MINDIFF, STATUS = 0, float('inf'), 0
for i in range(N):
    if T[i] > P[i]:
        STATUS |= 1
    elif T[i] < P[i]:
        STATUS |= 2
    RES += max(T[i], P[i])
    MINDIFF = min(MINDIFF, abs(T[i]-P[i]))
if STATUS != 3:
    RES -= MINDIFF

with open('prepare.out', 'w') as output:
    output.write(str(RES))
    output.write('\n')
