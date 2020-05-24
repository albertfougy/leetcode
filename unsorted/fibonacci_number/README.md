# 509. Fibonacci Number

The Fibonacci numbers, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
```
Given `N`, calculate `F(N)`.


## Approach 1: Recursion

Use recursion to compute the Fibonacci number of a given integer.


![](fibonacciRecursion5.png)
_Figure 1. An example tree representing what fib(5) would look like_

**Algorithm**

* Check if the provided input value, N, is less than or equal to 1. If true, return N.

* Otherwise, the function fib(int N) calls itself, with the result of the 2 previous numbers being added to each other, passed in as the argument. This is derived directly from the recurrence relation: `F n=F n−1+F n−2
​	
* Do this until all numbers have been computed, then return the resulting answer.


**Complexity Analysis**

* Time complexity : `O(2^N)`. This is the slowest way to solve the `Fibonacci Sequence` because it takes exponential time. The amount of operations needed, for each level of recursion, grows exponentially as the depth approaches N.

* Space complexity : `O(N)`. We need space proportionate to N to account for the max size of the stack, in memory. This stack keeps track of the function calls to `fib(N)`. This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a StackOverflowError. The Java docs have a good explanation of this, describing it as an error that occurs because an application recurses too deeply.

