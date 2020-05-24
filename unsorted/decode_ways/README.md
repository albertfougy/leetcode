# 91. Decode Ways

 A message containing letters from A-Z is being encoded to numbers using the following mapping:
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given a non-empty string containing only digits, determine the total number of ways to decode it.

## Solution
Insight: Started with the example of only 1's. For a string of length 1 there is one way to write it.

```
1
```
String of length 2 has two ways to write it.
```
1, 1
11
```
For a string of length 3 there are 3 ways to write it.
```
1, 1, 1
11, 1
1, 11
```
A string of length 4 has 5 ways to write it.
```
1, 1, 1, 1
11, 1, 1
1, 11, 1
1, 1, 11
11, 11
```

A pattern quickly emerges. `1, 2, 3, 5, ...` These are simply the fibonacci numbers. If only 1's or 2's are used in the string, the answer is the fibonacci number at (n+1). For some extra insight into why this is the case, look up the first discovery of the fibonacci numbers

"The Fibonacci sequence appears in Indian mathematics, in connection with Sanskrit prosody.[8][14] In the Sanskrit tradition of prosody, there was interest in enumerating all patterns of long (L) syllables that are 2 units of duration, and short (S) syllables that are 1 unit of duration. Counting the different patterns of L and S of a given duration results in the Fibonacci numbers: the number of patterns that are m short syllables long is the Fibonacci number Fm + 1.
` (https://en.wikipedia.org/wiki/Fibonacci_number#Origins)`

There are conditions associated with this problem though. The only valid encoded characters are 1->26. The way I thought about this that helped a lot is described as follows.

Take the example `s='11025'` and build up the solution from the beginning.
```
s = '1'
answer = 1 
(
1
)

s = '11'
answer = 2
(
1, 1
11
)

s = '110'
answer = 1
(
1, 10
)

s = '1102'
answer = 1
(
1, 10, 2
)

s = '11025'
answer = 2
(
1, 10, 2, 5
1, 10, 25
)
```
At each stage, if the last number is greater than 0, we can add it as a single element to all the possibilities from the previous solution. In addition, if the last two digit number is greater than 9 and less than 27, we can add all of the solutions from the previous solution that have a 'loner' element at the end. This can be summarized with the recurrence relation

```
F(n) = F(n-1) + F(n-2)                    if int(s_n) > 0 and 9<int(s_n-1 + s_n) < 27
     = F(n-1)                             if int(s_n) > 0
     = F(n-2)                             if 9<int(s_n-1 + s_n) < 27
     = 0                                  if int(s_n) == 0 and ! 9<int(s_n-1 + s_n)<27
F(1) = 1, F(0) =1

where s_n is the character at position n
```
