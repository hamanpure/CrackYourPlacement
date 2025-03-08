
class Solution:
    def longestPalindrome(self, s):
        # code here
        if not s:
            return ""
    
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return valid palindrome substring
    
        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd_pal = expandAroundCenter(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal
    
            # Even-length palindrome
            even_pal = expandAroundCenter(i, i + 1)
            if len(even_pal) > len(longest):
                longest = even_pal
    
        return longest


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends