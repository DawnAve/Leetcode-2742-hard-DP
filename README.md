# Leetcode-2742-hard-DP
A daily question on leecode, number 2742, is a hard question about recursion and dp, with less solution posted than usual

Here is the basic idea behind the solution:
Top-down dp
The solution is not long, but keep in mind that it is a dp-problem that usually doesn't have long code but requires deep thought.
A key detail to notice:
When a paid painter works for time T, the free painter can paint T walls, and the total cost will only be the cost for the paid
painter's wall. Therefore, we spent cost[i] to paint T+1 walls.

The core of dp problem is to find the dp-relationship, and the one in my solution is that you can either choose to paint the wall or not,
and the minimum cost will be min(paint, not paint) Clearly, if you don't paint the wall you won't even finish the task, but those braches
only serve as the "junk part" in dp problems. 

After that, we use dp(index, # of remaining walls) to find the minimum cost to paint the remaining walls. 

Hope you enjoy it!
