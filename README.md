# Stat-project
[Networking Again] 
Given n=50 people in a social network. Suppose any given unordered pair of two people are connected at random and independently with probability p:
(a) Generate and plot three network samples for each value of p in {0.02, 0.09, 0.12}. 
(b) Count the number of connections each vertex or node on a sample graph from the previous question. This statistic is the degree of the vertex. Plot a histogram of the vertex degrees for each of your sample graphs. 
(c) Vertex degree is supposedly binomially distributed for small network sizes. Generate a network with (n, p) = (100, 0.06) and plot a histogram of the vertex degrees. 

[Waiting] 
(a) Use the inverse CDF method to generate 1000 independent samples, Xi, of the exponential random variable with an average waiting time of 0.2 time units.  Evaluate the quality of your RNG with goodness of fit tests. 
(b) Each exponential random sample represents the waiting time until an event occurs. Implement a routine to count the number of exponentially-distributed time intervals that occur in 1 time unit. Generate such counts for 1000 separate unit time intervals. These counts distributed as Poisson distribution.

[Double Rejection] 
The random variable X has a bimodal distribution made up of an equally weighted, convex summation of a beta and a triangle distribution: f(x)=0.5×Beta(8,5),0<x≤1 
     0.5×(x−4),4<x≤5 
     −0.5×(x−6),5<x≤6 0,else 
Implement rejection sampling routines for X. Generate 1000 samples of the random variable using each envelope. Track the rejection rate of your rejection sampling RNGs. The rejection rate is the average number of rejected candidates per sample. This is a measure of the efficiency of your RNG.
