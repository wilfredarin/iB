"""
Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates.

Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time.

For example,

K = 3
N = 2
A = 6 5

Return: 14
At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates
At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates
At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate
so, total number of chocolates eaten: 6 + 5 + 3 = 14

Note: Return your answer modulo 10^9+7
"""
import heapq as hq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        for i in range(len(B)):
            B[i] = -B[i]
        hq.heapify(B)
        ans = 0
        while A>0:
            a = -hq.heappop(B)
            ans+=a
            a = a//2
            a = -a
            hq.heappush(B,a)
            A-=1
        return ans%(10**9+7)
