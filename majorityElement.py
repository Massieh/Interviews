"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """#my solution (O(nlogn)) :
        nums.sort()
        return nums[int(len(nums)/2)]
        """
        #Looked it up on internet :
        #Moore's voting is Space O(1) and time O(n) :
        x = 0
        y = 0
        for i in range (len(nums)):
            if x==0:
                y=nums[i]
            if y == nums[i]:
                x+=1
            else:
                x-=1
        return y