#User function Template for python3


class Solution:

    def Anagrams(self, words):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        l = list(set(["".join(sorted(i)) for i in words]))
        res = []
        
        for i in l:
            s = []
            for j in range(len(words)):
                if i == "".join(sorted(words[j])):
                    s.append(words[j])
            if s:
                res.append(s)
        return res
        
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.Anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends