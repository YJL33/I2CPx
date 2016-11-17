"""
Sorting
2.0 points possible (graded)
Input file:     sort.in
Output file:    sort.out
Time limit:     2 seconds
Memory limit:   256 megabytes

Given a sequence of integer numbers.
Your task is to sort it in a non-decreasing order using the mergesort algorithm.

To persuade us that you really use the mergesort algorithm, we ask you,
after performing a merge of a certain interval,
to print the endpoint indices and endpoint values of this interval.

Input

In the first line of the input file there is an integer n (1 <= n <= 100000),
the number of elements in the sequence.
The second line contains the sequence itself:
n integer numbers not exceeding 109 by their absolute value.

Output

The output file consists of several lines.
 
In the last line of the output file print the sequence after sorting.
Separate the numbers by single white spaces.

All the previous lines should describe the results of merges, one per line.
Every such line should contain four numbers: If Il Vf Vl,
where If is the starting index of the just-merged interval, Il is its ending index,
Vf is the value of the first element of the interval, Vl is the value of the last element.

Indices start with one, that is, 1 <= If <= Il <= n.
Please print the result of merges for the interval of size 1 as well.

If you print If Il X Y,
this means you have just merged a subsequence which corresponds to the [If;Il] subsequence of the original sequence.
In your particular implementation,
the real indices for the beginning and ending of this subsequence may vary,
but we nevertheless ask you to use this numbering scheme.

The merge descriptions can go in an arbitrary order,
not necessary coinciding with the order they are performed.
However, to improve performance,
we recommend to print these descriptions as soon as possible, not storing them in memory.
This is the reason why we ask to print the resulting array at the very end.

The correctness of the sorting scenario which you printed will be performed by a special checker program.
Every correct mergesort, which splits a subsequence into two smaller subsequences (not necessary equal!),
will be accepted if it manages to perform sorting within time and memory limits.
 
Note that every correct output will have 2n − 1 descriptions of merges, and for all 1
i n there will be a record i i ai  ai, where ai is the i-th element of the initial sequence. 
"""
import sys
import mmap

def mergesort(h, lst):                  # h: beginning index of list
    # merge sort body
    L = len(lst)
    if L == 1:                          # base case
        writedown(' '.join(map(str, [h+1, h+1, lst[0], lst[-1]])))
        return lst
    else:                               # recursive case, pass the original index to merger
        return merger(h, mergesort(h, lst[:int(L/2)]), mergesort(h+int(L/2), lst[int(L/2):]))

def merger(s, l, r):
    # merger
    # print('BEFORE', l+r)
    new, curl, curr = [], 0, 0
    # print('begin merging...')
    while curl < len(l) and curr < len(r):
        if l[curl] <= r[curr]:
            new += l[curl],
            curl += 1
        else:
            new += r[curr],
            curr += 1
    if curl < len(l): new += l[curl:]
    if curr < len(r): new += r[curr:]
    # print('AFTER', new)
    writedown(' '.join(map(str, [s+1, s+len(new), new[0], new[-1]])))
    return new

def writedown(line):
    # writer
    with open('sort.out', 'a') as output:
        output.write(line)
        output.write('\n')
        # print(line)
        return

with open('sort.in', 'r') as inputdata:             # read file
    MP = mmap.mmap(inputdata.fileno(), 0, access=mmap.ACCESS_READ)
    N = int(MP.readline())
    ORIGIN = [int(x.decode()) for x in MP.readline()[:-2].split()]

# while (True):
#     ORIGIN = ['1','100','10','1001','1000','11','12','13','111','110','1111','1110','1100']
#     ORIGIN = [x for x in map(int, ORIGIN)]
    # print('ORIGIN', ORIGIN, type(ORIGIN[0]))
    # print('SORTED:', sorted(ORIGIN))
#     ORIGIN2 = [str(x) for x in ORIGIN]
#     print('ORIGIN2', ORIGIN2)
    
    writedown(' '.join(map(str, mergesort(0, ORIGIN))))
    # break