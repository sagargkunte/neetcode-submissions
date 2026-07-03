class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alpha = [0] * 26

        for i in range(len(magazine)):
            alpha[ord(magazine[i]) - 97] += 1
        
        for i in range(len(ransomNote)):
            alpha[ord(ransomNote[i]) - 97] -= 1

            if alpha[ord(ransomNote[i])-97] < 0:
                return False
        return True
        
        
        