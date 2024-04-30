"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        Fibo = [1,1]
        for i in range (2,n+1):
            Fibo.append(Fibo[i-1]+Fibo[i-2])
        return Fibo[n]