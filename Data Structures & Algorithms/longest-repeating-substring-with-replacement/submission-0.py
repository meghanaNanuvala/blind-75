class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            # update
            res = max(res, r - l + 1)
        return res

        # l = 0
        # res = 0
        # maxf = 0
        # freq = {}

        # for r in range(len(s)):
        #     freq[s[r]] = 1 + freq.get(s[r], 0)
        #     maxf = max(maxf, freq[s[r]])            
            
        #     while (r - l + 1) - max(freq.values()) > k:
        #         freq[s[l]] -= 1
        #         l += 1
            
        #     # update
        #     res = max(res, r - l + 1)
        # return res



            



        