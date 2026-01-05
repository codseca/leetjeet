class Solution(object):
    def longestCommonPrefix(self, strs):
        
        prefix = ""  
        
        
        for i in range(len(strs[0])):
            letter = strs[0][i]
            
        
            for word in strs[1:]:
                if i >= len(word) or word[i] != letter:
                    return prefix
            
            prefix = prefix + letter
        
        return prefix
