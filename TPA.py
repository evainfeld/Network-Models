# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:37:16 2017

@author: eva
"""

import random
"""
import networkx as nx

import math
from math import factorial as fac
import itertools
"""
import matplotlib.pyplot as plt
import numpy


def Line(x):
    Line=[]
    for k in range(0,x+1):
        Line.append(0)
    for k in range(x+1,n):
        Line.append(random.randrange(2))
    return Line
        
def AddNode(X):
    global c
    H=[]
    global n
    for i in range(0,n):
        H.append([])
        for j in range(0,n):
            H[i].append(G[i][j])
        H[i].append(0)
    H.append([])
    for i in range(0,n+1):
        H[n].append(0)
    n=n+1
    c=c+1
    return H
    
def ProbabilityDistribution(X):
    global c
    w=c
    w=w
    PD=[]
    sum=0
    for j in range(0,n-1):
        D=0
        for i in range(0,n-1):
            D=D+X[i][j]
        PD.append(D)
    for j in range(0,n-1):
        if G[n-1][j]==1:
            for i in range(0,n-1):
                if G[j][i]==1:
                    PD[i]=PD[i]+w
    for j in range(0,n-1):
        sum=sum+PD[j]
    for j in range(0,n-1):
        d=PD[j]*1.0/sum
        PD[j]=d
    return PD
    
def CreateLink(X):
    A=numpy.random.choice(numpy.arange(0, n-1), p=ProbabilityDistribution(X))
    while  G[A][n-1]==1:
            A=numpy.random.choice(numpy.arange(0, n-1), p=ProbabilityDistribution(X))
    G[A][n-1]=1
    G[n-1][A]=1

   
def DegreeDistribution(X):
    PD=[]
    for j in range(0,n-1):
        D=0
        for i in range(0,n-1):
            D=D+X[i][j]
        PD.append(D)
    PDD=[]
    for j in range(0,n-1):
        PDD.append(0)
    for j in range(0,n-1):
        PDD[PD[j]]=PDD[PD[j]]+1
    return PDD
    
def LocalClustering(X):
    l=len(X)
    C=[]
    for v in range(l):
        d=0.0
        C.append(0.0)
        for i in range(l):
            if X[v][i]==1:
                d=d+1
                for j in range(i,l):
                    if X[v][j]==1:
                        if X[i][j]==1:
                            C[v]=C[v]+1
        D=d*(d-1)/2
        if C[v]!=0:
            C[v]=C[v]/D
    return C
    
def OverallClustering(Y):
    l=len(Y)
    c=0.0
    for i in range(l):
        c=c+Y[i]
    return c/l
                                
def Density(X):
    l=len(X)
    E=0.0
    for v in range(l):
        for i in range(v):
            if X[v][i]==1:
                E=E+1
    D=l*(l-1)/2
    return E/D
    
    
    


G=[]
n=input('Enter the desired number of nodes in the seed graph: ')
m=input('Enter the desired parameter m: ')
M=input('Enter the desired total number of nodes: ')-n
global c
c=n    

for i in range(0,n):
    G.append(Line(i))
    for j in range(0,n):
        if i>j and G[j][i]==1:
            G[i][j]=1
    
for o in range(0,M):
    G=AddNode(G) 
    for i in range(0,m):
        CreateLink(G)  

N=LocalClustering(G)
O=OverallClustering(N)
    

P=DegreeDistribution(G)
plt.plot(P)

Density=Density(G)
Dens=str(Density)
N=str(n)
o=str(O)

print "TPA on "+N+" nodes"
print
print "The local clustering coefficient is "+o
print 
print "Density is "+Dens
print
print "The degree distribution in this graph is:"
