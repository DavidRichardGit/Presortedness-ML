# Presortedness-ML
Predicting the optimal sorting algorithm for specific arrays with given presortedness metrics

## Optimality of a sorting algorithm

The efficiency of a sorting algorithm can be captured from multiple different angles. The fastest might not always be the first choice, since there are other important measures of an algorithm, such as memory complexity, stability or wheter an algorithm can handle a constant stream of input or not. The time complexity is hard to inspect, because there are many factors playing into it: the type of data, the size of the data, the cost of comparing and swapping values, the hardware etc. Another aspect which makes it hard to investigate the time complexity is the implementation of the algorithm. Comparing any self-implemented sorting algorithm (can be the most efficient one) in python to the .sort() function that uses timsort does not make sense, since timsort will outperform by a large margin. This is due to the fact that the .sort() function is written in C, highly optimized and doesn't have to be interpreted line-by-line (see [here](https://github.com/DavidRichardGit/Presortedness-ML/blob/main/pythonTimsort%20(2).ipynb)).

This is why i will be focusing on the comparison complexity, it is not dependent on the hardware and the implementation. Additionally it is a good predictor of the computational complexity of an algorithm.

## Presortedness

For a sorting algorithm to be considered optimal for a presorted array the algorithm has to be adaptive. Adaptive means that the algorithm performs asymptotically optimal on an already sorted array. 
Arrays of numbers can be sorted or almost sorted in different ways. Measures of presortedness helps us describe how sequences are arranged to get insight about the data.
Formally the following conditions formulated by Marcello La Rocca and Domenico Cantone in _NeatSort, a practical adaptive algorithm_ have to be satisfied: 

Given two sequences X and Y of distinct elements, a metric of presortedness M is a function that satisfies the following axioms:

* If X is sorted, then M(X) = 0
* If X and Y are order isomorphic, then M(X) = M(Y)
* If X is a subset of Y, then M(X) ≤ M(Y)
* If every element of X is smaller than every element of Y, then M(X.Y) ≤ M(X) + M(Y)
* M({x}.X) ≤ |X| + M(X) for every natural integer X

Similarly to the general adaptivity of an algorithm an adaptive algorithm with respect to a certain measure of presortedness is defined as follows by Svante Carlsson, Christos Levcopoulos and Ola Petersson in _Sublinear Merging and Natural Mergesort_:

*A sorting algorithm is said to be adaptive with respect to a measure of presortedness if it sorts all sequences, but performs particularly well on those having a high degree of presortedness according to the measure.*

Some relation of presortedness metrics can be visualized by this graph from O. Petersson and A. Moffat in _A framework for adapative sorting_. The metric on the upper node is algorithmically finer than the one connected lower node. If a metric f<sub>1</sub> is algorithmically finer than another metric f<sub>2</sub> it means, that an f<sub>1</sub> optimal sorting algorithm is automatically f<sub>2</sub> optimal.

![Image Alt Text]([https://imgur.com/SnTLZeh](https://imgur.com/a/nWjvzMS))

To get the maximum amount of infomation about the way an array is arranged it makes sense to have a well distributed set of metrics.
