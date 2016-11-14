"""
Generate Tests!
2.0 points possible (graded)
Input file:     testgen.in
Output fole:    testgen.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Input

The first line contains a single integer number K (2 <= K <= 10^7).

Output

Output the number of maximal tests for this problem with the constraint K.
"""

# List of highly compound numbers, key = number, value = divisors.
DCTHCN = {1:1,2:2,4:3,6:4,12:6,24:8,36:9,48:10,60:12,120:16,180:18,240:20,360:24,\
    720:30,840:32,1260:36,1680:40,2520:48,5040:60,7560:64,10080:72,15120:80,20160:84,\
    25200:90,27720:96,45360:100,50400:108,55440:120,83160:128,110880:144,166320:160,\
    221760:168,277200:180,332640:192,498960:200,554400:216,665280:224,720720:240,1081080:256,\
    1441440:288,2162160:320,2882880:336,3603600:360,4324320:384,6486480:400,7207200:432,\
    8648640:448,10810800:480}


with open('testgen.in', 'r') as inputdata:
    K = int(inputdata.readline())
    RES, cur = 1, 0
    P = sorted(DCTHCN.keys())
    for k in P:
        if k <= K:
            RES = k
        else:
            break

with open('testgen.out', 'w') as output:
    output.write(str(K-RES+1))
    output.write('\n')
