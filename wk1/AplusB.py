"""
A + B
2.0 points possible (graded)
Input ﬁle:      aplusb.in
Output ﬁle:     aplusb.out
Time limit:     2 seconds
Memory limit:   256 megabytes


Given two integer numbers, A and B, output A + B.

Input

The input ﬁle contains one line with two integer numbers, A and B (−109 <= A,B <= 109),
separated by one whitespace.

Output

Output A + B in the ﬁrst and only line of the output ﬁle.
"""
with open('aplusb.in', 'r') as input:
    a, b = [int(x) for x in input.readline().split(' ')]
with open('aplusb.out', 'w') as output:
    output.write(str(a + b))
    output.write('\n')