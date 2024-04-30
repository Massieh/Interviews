"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.Recherche(nums,0,len(nums)-1,target)


    def Recherche(self,nums,inf,sup,target):
        if sup < inf :
            return inf
        mid = int((sup + inf) / 2)
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            return self.Recherche(nums,inf,mid-1,target)
        return self.Recherche(nums,mid+1,sup,target)
