"""
Put the Chairs the Right Way!
2.0 points possible (graded)
Input file:     chairs.in
Output fole:    chairs.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Input

The input file contains three positive integer numbers not exceeding 100
- the lengths of sides of the table.
It is guaranteed that such a table will have a non-zero area.

Output

Output the average distance between the middle points of the sides of the table,
which was described in the input.
Any answer, which differs from the correct one by not more than 10-6, will be accepted.
"""
with open('chairs.in', 'r') as inputdata:
    C = [int(x) for x in inputdata.readline().split(' ')]

# just divide avg of sides by 2
with open('chairs.out', 'w') as output:
    output.write(str(sum(C)/6))
    output.write('\n')
