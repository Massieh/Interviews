"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        compteur =0
        while (compteur*compteur <=x):
            compteur+=1
        return compteur-1
