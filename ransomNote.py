"""
Keep in mind that this is either training for interviews or an interview itself.
The code might not be commented and the variable naming might be questionable at times since it's not the point of those.
The name of the file is most times than none a good hint as to what the purpose of the exercise is
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        compteur={}
        for letter in magazine:
            if letter not in compteur:
                compteur[letter]=0
            compteur[letter]+=1
        
        for letter in ransomNote:
            if letter not in compteur:
                return False
            compteur[letter]-=1
        
        for elem in compteur.values():
            if elem <0:
                return False
        return True