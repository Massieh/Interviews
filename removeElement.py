"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=0
        i=0
        while (i <len(nums)):
            if nums[i]!=val:
                x+=1
            else:
                nums.pop(i)
                i-=1
            i+=1
        return x
