#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # Code here
        words.sort(key=len)
        word_map = {}  # Dictionary to store the longest chain for each word
        max_length = 1
        
        for word in words:
            length = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]  # Remove one character to check predecessor
                if pred in word_map:
                    length = max(length, word_map[pred] + 1)
            word_map[word] = length
            max_length = max(max_length, length)
        
        return max_length
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends