# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


---

# Solution
---
## Approach 1: Elementary Math

**Intuition**

Keep track of the carry using a variable and simulate digits-by-digits sum starting from the head of list, which contains the least-significant digit.


![alt text](2_add_two_numbers.svg)

_Figure 1. Visualization of the addition of two numbers: 342 + 465 = 807342+465=807.
Each node contains a single digit and the digits are stored in reverse order._

Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1l1 and l2l2. Since each digit is in the range of 0 \ldots 90…9, summing two digits may "overflow". For example 5 + 7 = 125+7=12. In this case, we set the current digit to 22 and bring over the carry = 1carry=1 to the next iteration. carrycarry must be either 00 or 11 because the largest possible sum of two digits (including the carry) is 9 + 9 + 1 = 199+9+1=19.

The pseudocode is as following:

* Initialize current node to dummy head of the returning list.
* Initialize carry to 00.
* Initialize pp and qq to head of l1l1 and l2l2 respectively.
* Loop through lists l1l1 and l2l2 until you reach both ends.
    * Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
    * Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
    * Set sum = x + y + carrysum=x+y+carry.
    * Update carry = sum / 10carry=sum/10.
    * Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
    * Advance both pp and qq.
* Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.
* Return dummy head's next node.


Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

Take extra caution of the following cases:

**Test case**	            **Explanation**
l1=[0,1]l1=[0,1]
l2=[0,1,2]l2=[0,1,2]	When one list is longer than the other.
l1=[]l1=[]
l2=[0,1]l2=[0,1]	    When one list is null, which means an empty list.
l1=[9,9]l1=[9,9]
l2=[1]l2=[1]	        The sum could have an extra carry of one at the end, which is easy to forget.