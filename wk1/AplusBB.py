"""
A + B^2
2.0 points possible (graded)
Input ﬁle:      aplusbb.in
Output ﬁle:     aplusbb.out
Time limit:     2 seconds
Memory limit:   256 megabytes


Given two integer numbers, A and B, output A + B^2.

Input

The input ﬁle contains one line with two integer numbers, A and B (−10^9 <= A,B <= 10^9),
separated by one whitespace.

Output

Output A + B^2 in the ﬁrst and only line of the output ﬁle.
"""
with open('aplusbb.in', 'r') as input:
    a, b = [int(x) for x in input.readline().split(' ')]
with open('aplusbb.out', 'w') as output:
    output.write(str(a + b*b))
    output.write('\n')