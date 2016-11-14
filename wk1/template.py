"""
Write a Code Template!
2.0 points possible (graded)
Input file:     template.in
Output fole:    template.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Input

The first line of the input file contains two integer numbers W and H (1 <= W,H <= 100)
- the width and the height of the keyboard.
The next H lines contain W ASCII symbols each with possible codes from 32 to 126 inclusively.
These lines determine the keyboard.
Each symbol occurs at most once.
There is a blank line after the keyboard description.

After this, three block of code template description follow.
The first line of each block is the name of the programming language.
The name of the programming language does not exceed 100 characters,
and may contain ASCII symbols from 32 to 126.
The code template itself follows in several subsequent non-empty lines (at least one).
The block ends with an empty line.

The number of symbols in every code template does not exceed 10000 (without newline characters).
Every symbol in a template will exist on the keyboard described in the beginning of the input file.

Output

In the first line of the output file print the name of the language of the code template,
which the team should choose.
The second line should contain the time needed to type the chosen code template.
If there are several possible code templates with the same time,
output the one which comes first in the input file.
"""
with open('template.in', 'r') as inputdata:
    W, H = [int(x) for x in inputdata.readline().split(' ')]    # get the dimension
    DCTX, DCTY = {}, {}
    for i in range(H):
        ROW = inputdata.readline()
        for j in range(W):
            c = ROW[j]
            DCTY[c], DCTX[c], j = H-i, j+1, j+1         # give each char its coordinate
    # print(DCTX)
    # print(DCTY)
    L, NAME, D = 0, [], [0 for _ in range(3)]           # Name & D: Name and distance of Language
    assert inputdata.readline() in ["\n", "\r\n"]       # skip this blank line
    while L < 3:
        NAME += inputdata.readline(),                   # get the Language name
        # NEXTLINE = inputdata.readline()
        NEXTLINE, LAST = inputdata.readline(), None
        while NEXTLINE not in ["\n", "\r\n"]:           # Language template
            if LAST:                                    # Don't ignore distance while change line
                D[L] += max(abs(DCTY[NEXTLINE[0]]-DCTY[LAST]), abs(DCTX[NEXTLINE[0]]-DCTX[LAST]))
            for i in range(len(NEXTLINE)-2):
                c1, c2 = NEXTLINE[i], NEXTLINE[i+1]
                D[L] += max(abs(DCTY[c2]-DCTY[c1]), abs(DCTX[c2]-DCTX[c1]))
            LAST = NEXTLINE[-2]
            NEXTLINE = inputdata.readline()
        L += 1

    # print(NAME, str(NAME[D.index(min(D))]))
    # print(D, str(min(D)))

with open('template.out', 'w') as output:
    output.write(str(NAME[D.index(min(D))]))
    output.write(str(min(D)))
    output.write('\n')
