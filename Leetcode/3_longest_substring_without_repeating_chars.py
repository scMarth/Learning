class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print("input: " + s)
        longest_substring = ""
        
        start = 0
        while start <= len(s) - 1:

            curr_char = s[start]
            char_hash = {}
            char_hash[curr_char] = True

            end = start + 1
            while end <= len(s) - 1:
                if s[end] in char_hash:
                    break
                else:
                    char_hash[s[end]] = True
                end += 1

            print(s[start:end])
            print("\tstart: " + str(start))
            print("\tend: " + str(end))

            if s[end - 1] == s[end]:
                start = end - 1
            else:
                start = end



sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print("")
print(sol.lengthOfLongestSubstring("bbbbb"))
print("")
print(sol.lengthOfLongestSubstring("pwwkew"))
print("")
print(sol.lengthOfLongestSubstring("auuwx"))
print("")
print(sol.lengthOfLongestSubstring("dvdf"))

