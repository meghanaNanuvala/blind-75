class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxS = 0
        freq = Counter()

        for r in range(len(s)):
            ch = s[r]
            freq[ch] += 1
            # print(freq)

            # if duplicate is found, shrink from the left
            while freq[ch] > 1:
                freq[s[l]] -= 1
                if freq[s[l]]== 0:
                    del freq[s[l]]
                l += 1
            
            # 'r' expands automatically via for loop
            maxS = max(maxS, r-l+1)

        return maxS




            

