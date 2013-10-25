#!/usr/bin/python
import hsr
#generate decision tree data
data = hsr.HSRkqStruct(5,7)
print data
# convert the tree data to edge list
edgelist = hsr.data2edgeList(data)
# draw these edge list
hsr.drawGraph(edgelist)
