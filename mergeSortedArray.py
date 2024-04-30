"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if (n<1):
            return
        index = m + n - 1
        m=m-1
        n=n-1
        while index>=0:
            if m >=0 and nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -=1
            elif n >=0:
                nums1[index] = nums2[n]
                n -=1
            index -=1
