"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        x=(len(nums)-k)%len(nums)
        res=nums[x:] + nums[:x]
        nums.clear()
        nums.extend(res)
        """ Space O(1)
        x=(len(nums)-k)%len(nums)
        for i in range (x):
            nums.append(nums[0])
            nums.pop(0)
        """
