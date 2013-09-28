#!/usr/bin/python
import hsr
#generate data

data = hsr.HSRkqStruct(5,7)
print data
edgelist = hsr.data2edgeList(data)
hsr.drawGraph(edgelist)
