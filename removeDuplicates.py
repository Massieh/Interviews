"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while (i< len(nums)):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        return i
        
