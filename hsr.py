import sys
import math
import numpy 
import networkx as nx
import matplotlib.pyplot as plt
import json
  
def hsrNK(rungs,questions):
  if rungs == 1:
    return 0
  elif rungs >= 2 and questions == 1:
    return rungs - 1
  minn = sys.maxint
  for i in range(1,rungs):
    result = 1 + max(hsrNK(rungs-1,questions-1), hsrNK(rungs-1,questions))
    if result < minn:
      minn = result
  return minn
#calculate the highest value for rungs
def hsrKQ(jars,questions):
  if jars == 0 or questions == 0:
    return 0
  return 1 + hsrKQ(jars - 1, questions - 1) + hsrKQ(jars, questions-1)
# calculate the minimum question may be asked for rung q, kars k
def MinT(n,k):
  s = numpy.zeros((n+1,k+1),dtype = numpy.int8)
  m = numpy.zeros((n+1,k+1),dtype = numpy.int8)
  if n ==0 or k == 0:
    return 0,s
  if k == 1:
    for i in range(1,n+1):
      s[i,1]=1
    return n,s
  for i in range(1,n+1):
    m[i,1] = i
    s[i,1] = 1
  for i in range(1,n+1):
    for j in range(2,k+1):
      m[i,j] = sys.maxint
      for a in range(1,i+1):
        q = 1 + max(m[a-1,j-1],m[i-a,j])
        if q < m[i,j]:
          m[i,j] = q
          s[i,j] = a
  return int(m[i,j]),s

def trace(n,k,s,start):
  if k <= 0 or n <= 0:
    return json.dumps({'h' : start})
  a = int(s[n,k]) + start 
  return json.dumps([a,json.loads(trace(a-1,k-1,s,start)),json.loads(trace(n-a,k,s,a))])

def jsonTrace(n,k,s):
  return '{\"decision_tree\" : ' + trace(n,k,s,0) +'}'



#Build the highest rungs tree given jars and questions
def HSRkqStruct(jars,questions):
  maxs = sumBino(jars,questions)
  return HSRkqStructHelper(jars,questions,0,(maxs-1))
def HSRkqStructHelper(jars, questions,starts,ends):
  if jars ==0 or questions == 0 or starts >= ends:
    return ['H' + str(starts),[],[]]
  leftsize = sumBino(jars - 1,questions - 1);
  rightsize = sumBino(jars,questions-1)
  l = HSRkqStructHelper(jars - 1, questions - 1,starts,starts + leftsize -1)
  r = HSRkqStructHelper(jars,questions - 1,starts + leftsize,ends)
  root = [starts + leftsize,l,r]

  return root
#return child number
def lchild(num):
  return 2*num +1
def rchild(num):
  return 2*num +2
#return the binomial(q,i)
def sumBino(k,q):
  if q == 0 or k == 0:
    return 1
  if q == 1 and k > 0:
    return 2
  if k > q:
    k,q = q,k
  summ = 0
  for i in range(0,k + 1):
    summ += binomial(q,i)
  return summ
def binomial(q,i):
  result = math.factorial(q) / (math.factorial(q-i) * math.factorial(i))
  return result

#convert data to edgelist
def data2edgeList(data):
  edgelist = []
  generatelist(data,edgelist)
  return edgelist

def generatelist(data,edgelist):
  if len(data) == 0 :
    return
  else:
    if valueExist(data[1]):
      edgelist.append([data[0],getvalue(data[1])])
      generatelist(data[1],edgelist)
    if valueExist(data[2]):
      edgelist.append([data[0],getvalue(data[2])])
      generatelist(data[2],edgelist)
  return 
def getvalue(data):
  return data[0]
def valueExist(data):
  return not len(data) == 0
#drawGraph
def drawGraph(edgelist):
  G = nx.Graph() 
  G.add_edges_from(edgelist)
  pos = nx.graphviz_layout(G,prog='twopi',root = 4,args='')
#  pos = graph_layout(edgelist)
  plt.figure(figsize=(15,20))
  nx.draw(G,pos,node_size=100,alpha=0.1,node_color='blue',with_labels=True)
  plt.axis=('equal')
  plt.savefig('hsr_graph.png')
  plt.show()

def graph_layout(edgelist):
  pos ={}
  visited = []
  level = 0
  HOFF = 1500
  XOFF = 200
  WIDTH = 300
  HEIGHT = 3
  XSTART = 1500 
  edge = edgelist[0]
  subnodes = [edge[0]]
  pos[subnodes[0]] = tuple([XSTART, HOFF])
  level += 1
  dicEdge = getDicEdge(edgelist)
  while not len(subnodes) == 0:
    tempnodes = []
    x = XSTART - level * XOFF 
    count = 0
    for node in subnodes:
      if node in visited:
        continue
      children = dicEdge[node]
      visited.append(node)
      if len(children) == 0:
        continue
      tempnodes.extend(children)
      for child in children:
        pos[child] = tuple([x + count * WIDTH,HOFF - level * HEIGHT])
        count +=1
    subnodes = tempnodes
    level += 1
  return pos
def getDicEdge(edgelist):
  dic = {}
  for edge in edgelist:
    if dic.has_key(edge[0]):
      (dic.get(edge[0])).append(edge[1])
    else:
      dic[edge[0]] = [edge[1]]
    if not dic.has_key(edge[1]):
      dic[edge[1]] = []
  return dic
