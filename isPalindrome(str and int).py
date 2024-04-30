"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #With conversion to str
        x=str(x)
        return x[::-1]==x
        """
        #Without Conversion
        if x<0:
            return False
        sup=10
        while (x>=sup):
            sup*=10
        sup=sup/10
        inf=1
        while (inf < sup):
            x_inf=int(x/inf)
            x_inf=x_inf%10
            x_sup=int(x/sup)
            x_sup=x_sup%10
            if (x_inf != x_sup):
                return False
            inf*=10
            sup=sup/10
        return True
        """
  