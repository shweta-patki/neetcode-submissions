class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost==[]:
            return 0
        bestcost = [0]*len(cost)
        bestcost[0] = cost[0]
        bestcost[1] = cost[1]
        for i in range(2, len(cost)):
            bestcost[i] = min(bestcost[i-1]+cost[i], bestcost[i-2]+cost[i])
        return min(bestcost[-1], bestcost[-2])