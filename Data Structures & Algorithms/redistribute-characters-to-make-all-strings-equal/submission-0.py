class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        char_counts = Counter("".join(words))
        
        for count in char_counts.values():
            if count % n != 0:
                return False
        return True