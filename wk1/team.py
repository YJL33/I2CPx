"""
Create a Team!
2.0 points possible (graded)
Input file:     team.in
Output file:    team.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Input

The input file contains three lines,
each containing three integer numbers - the table which the guys constructed.
All numbers are positive and do not exceed 1000.

Output

Output one number - the maximum effiency which this team may achieve by optimal role distribution.
Any answer, which is different from the correct one by no more than 10-6, is accepted.

Examples
team.in     team.out
1 1 1

1 1 1

1 1 1       1.7320508075688772

1 2 3

6 5 4

7 8 9       11.0
"""
import itertools
with open('team.in', 'r') as inputdata:
    PLAYERA = [int(x) for x in inputdata.readline().split(' ')]
    PLAYERB = [int(x) for x in inputdata.readline().split(' ')]
    PLAYERC = [int(x) for x in inputdata.readline().split(' ')]

# compare all square sum of permutations
RES = 0
for i, j, k in itertools.permutations(range(3)):
    RES = max(RES, PLAYERA[i]*PLAYERA[i]+PLAYERB[j]*PLAYERB[j]+PLAYERC[k]*PLAYERC[k])

with open('team.out', 'w') as output:
    output.write(str(RES**0.5))
    output.write('\n')
