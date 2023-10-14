class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dp(i, remain):
            if (remain<=0):
                return 0
            if i == n:
                return inf
            
            paint = (cost[i]+dp(i+1, remain - 1 - time[i]))
            xpaint = dp(i+1, remain)
            return min(paint, xpaint)

        return dp(0,n)
