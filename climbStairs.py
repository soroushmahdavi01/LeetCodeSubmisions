class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 1
        previous = 0
        holder = 0
        for i in range(int(n)):
            holder = previous
            previous = answer
            answer = holder + previous
        return(answer)
        
