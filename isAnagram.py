"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        compteur={}
        for x in s:
            if x not in compteur:
                compteur[x]=0
            compteur[x]+=1
        for x in t:
            if x not in compteur:
                return False
            compteur[x]-=1
        for elem in compteur.values():
            if elem !=0:
                return False
        
        return True