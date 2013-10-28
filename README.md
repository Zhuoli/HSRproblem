HSRproblem
HSR(n,k,q): you are given k jars and allowed try q times to find the maximal rungs.

1: The HSRkqStruct method can calculate the maxmimal rungs given k jars and allowed to try q times and The data2edgeList can generate a list of edge of decision tree then the drawGraph method can draw a graph of this tree to demenstrate it

2: the hsrNK method can calculate the minimal tries needed to judge N rungs given n rungs

Instruction:

Usage: #> ./hsr.py <rungs n> <Jars k> /

Output: 1： The optimal q for MinT
        2： The Json string for this decision tree
        3:  A file named 't-n-k.txt' which contains the Json string

