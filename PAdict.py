# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:51:15 2016

@author: eva
"""
import random
import numpy

graph={}
n=input('Enter the desired number of nodes in the seed graph: ')
m=input('Enter the desired parameter m: ')
N=input('Enter the desired total number of nodes: ')-n

def SeedGraph(x):
    prob=m*1.0/n
    graph[0]=[]
    for i in range(1,x):
        graph[i]=[]
        for j in range(i):
            coin=numpy.random.choice(numpy.arange(0, 2), p=[1-prob,prob])
            if coin==1:
                graph[j].append(i)
                graph[i].append(j)
                
def AddNode():
    global n
    global graph
    graph[n]=[]    
    n=n+1

 
def AddLinks():
    global graph
    PD=CurrentProbability()
    for i in range(m):
        A=numpy.random.choice(numpy.arange(0, n), p=PD)
        while  A in graph[n-1]:
            A=numpy.random.choice(numpy.arange(0, n), p=PD)
        graph[A].append(n-1)
        graph[n-1].append(A)
    
def CurrentProbability():
    Degrees=[]
    for i in graph:
        Degrees.append(len(graph[i]))
        SumOfDegrees=0
        for i in Degrees:
            SumOfDegrees=SumOfDegrees+i
        ProbabilityDistribution=[]
    for i in Degrees:
        A=i*1.0/SumOfDegrees
        ProbabilityDistribution.append(A)
    return ProbabilityDistribution
           

SeedGraph(n)
for k in range(N):
    AddNode()
    AddLinks()
print graph
    


