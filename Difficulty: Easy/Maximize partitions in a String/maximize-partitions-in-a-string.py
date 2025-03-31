class Solution:
    def maxPartitions(self , s):
        # code here
        last_occurrence = {char: i for i, char in enumerate(s)}  # Store last occurrence of each character
        partitions = 0
        max_end = 0
        start = 0
        
        for i, char in enumerate(s):
            max_end = max(max_end, last_occurrence[char])  # Update max end index
            if i == max_end:  # If current index reaches the partition end
                partitions += 1
                start = i + 1  # Start new partition
    
        return partitions

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends