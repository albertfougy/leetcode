# Using greedy strategy, we want to remove such digit that with higher base d (10^d) 
# and with higher value itself comparing to its successor. So we can use a monotonic 
# queue and keep rolling out the value we want to remove, also keep an eye on k 
# because we don't want to remove more than k digits.
# If no such complete removal( must be k times) happend (none or less than k times, hence the break - else flow), 
# it means that some ratty digit(s) remain in the list and it forms a monotonically 
# increasing trend, so we need to pop them off from tail.
# Also you need to deal with heading zeros.

def removeKdigits(self, num: 'str', k: 'int') -> 'str':
        if not k:
            return num
        Q=collections.deque()
        for i in range(len(num)):
            while Q and num[i]<Q[-1] and k>0:
                k-=1
                Q.pop()
            Q.append(num[i])
            if k<=0:
                Q+=list(num[i+1:])
                break
        else:
            while(k>0):
                Q.pop()
                k-=1
        while(Q and Q[0]=='0'):
            Q.popleft()
        return ''.join(Q) if Q else '0'