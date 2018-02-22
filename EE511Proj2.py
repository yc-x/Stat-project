import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import numpy as np
import scipy
from scipy import stats
from scipy.stats import chisquare

"""-----------------------------------
   EE511 Project 2 made by Yuncong Xie

   Need to close the previous figure to
   continue the program or check the next
   figure.
   The third part takes very long time if
   given a large input.
   -----------------------------------"""

def less_count(a):
    counter = 0
    for x in a:
        if x < 1:
            counter = counter + 1
    return counter

def pdf(x):
    """The pdf in given third part"""
    if 0 < x <= 1:
        y = 0.5 * (stats.beta.pdf(x,8,5))
    elif 4 < x <=5:
        y = 0.5 * (x - 4)
    elif 5 < x <= 6:
        y = - 0.5 * (x - 6)
    else:
        y = 0
    return y

def prob(p):
    """probability generator by using random number"""
    a = random.random()
    if a < p:
        b = 1
    elif a>= p:
        b = 0
    return b

def Net_Again(n,p):
    """The first part of project"""
    G = nx.Graph()
    G.clear()
    H = nx.path_graph(n)
    G.add_nodes_from(H)
    for i in range (0,n):
        for j in range (i+1,n):
            e = (i,j)
            if prob(p) == 1:
                G.add_edge(*e)
            elif prob(p) == 0:
                continue
    nx.draw(G,pos = nx.circular_layout(G),node_size = 30)
    plt.show()
    a = G.degree()
    print(a)
    c = []
    for b in a:
        c.append(b[1])
    print(c)
    plt.hist(c,bins = max(c)-min(c)+1,histtype = 'bar', rwidth = 1, edgecolor = 'black')
    plt.xlabel('The degree of nodes')
    plt.ylabel('Frequency(in number)')
    #plt.xlim(0,n-1)
    plt.show()
    k = np.arange(0,21)
    binomial = stats.binom.pmf(k,100,0.06)
    plt.plot(k,binomial)
    plt.xlabel('Binomial of n=100,p=0.06')
    plt.ylabel('Frequency')
    plt.show()
    plt.clf()

def Wait():
    """The second part of the project"""
    c = []
    for n in range (1,1001):
        a = random.random()
        b = -(math.log(1-a))/5
        c.append(float(b))
    plt.hist(c,histtype = 'bar',edgecolor = 'black')
    plt.xlabel("The sample generated")
    plt.ylabel("Frequency(in number)")
    n,bins,patches = plt.hist(c,histtype = 'bar',edgecolor = 'black')
    print(n)
    print(bins)
    cdf = []
    for i in range (0,len(bins)-1):
        x = 1000*(math.pow(math.e,-5 * bins [i]) - math.pow(math.e,-5*bins[i+1])) 
        cdf.append(x)
    f = scipy.stats.chisquare(np.array(n),cdf,ddof = 0)
    print(f)
    sigma = 0
    for j in range (0,len(n)):
        sigma = ((np.square(n[j] - cdf[j]))/(cdf[j])) + sigma
    print(sigma)
    plt.show()
    plt.clf()

def wait_2():
    """The 2nd problem of second part"""
    z = []
    c = []
    for j in range(1,1001):
        counter = 0
        valve = 0
        while valve <= 1:
            a = random.random()
            b = -(math.log(1-a))/5
            valve = valve + b
            counter = counter + 1
        counter = counter - 1
        c.append(counter)
    print(c)
    plt.hist(c,histtype = 'bar',edgecolor = 'black')
    plt.xlabel("The nmubers of events happens accumulate 1 time unit")
    plt.ylabel("Frequency(in numbers)")
    plt.show()
    n = np.arange(0,16)
    poisson = stats.poisson.pmf(n,5)
    plt.plot(n,poisson)
    plt.xlabel('Poisson pmf of lamda=5')
    plt.ylabel('Frequency')
    plt.show()
    plt.clf()

def Double_Rej(q):
    """The third part of the project"""
    a = []
    b = []
    f = []
    cnt_1 = []
    cnt_2 = []
    for m in range (1,q+1):
        counter_1 = 0
        total_1 = 0
        counter_2 = 0
        total_2 = 0
        while counter_1 < 1000:
            x = random.uniform(0,1)
            d = random.uniform(0,1.6)
            total_1 = total_1 + 1
            if d <= pdf(x):
                a.append(x)                    #random number generated from the first envelope
                counter_1 = counter_1 + 1
        while counter_2 < 1000:
            y = random.uniform(4,6)
            g = random.uniform(0,0.5)
            total_2 = total_2 + 1
            if g <= pdf(y):
                f.append(y)                    #random number generated from the second envelope
                counter_2 = counter_2 + 1
        c_1 = (total_1 - counter_1)/(total_1)
        c_2 = (total_2 - counter_2)/(total_2)
        cnt_1.append(c_1)
        cnt_2.append(c_2)
        plt.hist(a,histtype = 'bar',edgecolor = 'black')
        plt.xlabel('number remains in rejection in a single sample')
        plt.ylabel('Frequency')
        plt.hist(f,histtype = 'bar',edgecolor = 'black')
        plt.xlabel('number remains in rejection in a single sample')
        plt.ylabel('Frequency')
        plt.show()
    print("The average rejection rate of 1st envelope is:")
    print(sum(cnt_1)/len(cnt_1))
    print("The average rejection rate of 2nd envelope is:")
    print(sum(cnt_2)/len(cnt_2))

n = input("Please input the number of nodes:")
p = input("Please input the probability:")
Net_Again(int(n),float(p))
Wait()
wait_2()
q = input("Please input the time of samples needed:")
Double_Rej(int(q))
