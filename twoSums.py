"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted=sorted(nums)
        inf=0
        sup=len(nums)-1
        while(nums_sorted[inf]+nums_sorted[sup]!=target):
            if (nums_sorted[inf]+nums_sorted[sup]<target):
                inf+=1
            else:
                sup-=1
        res=[]
        for i in range (len(nums)):
            if nums[i]==nums_sorted[inf] or nums[i] == nums_sorted[sup]:
                res.append(i)
        return res
