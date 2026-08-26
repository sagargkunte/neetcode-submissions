class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str_ = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                str_ += word1[i]
            if i < len(word2):    
                str_ += word2[i]
            i += 1
        return str_