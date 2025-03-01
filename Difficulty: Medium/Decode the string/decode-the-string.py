
class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit numbers
            elif char == "[":
                stack.append((current_str, num))  # Save current state
                current_str, num = "", 0  # Reset for new substring
            elif char == "]":
                last_str, repeat_count = stack.pop()  # Retrieve last saved state
                current_str = last_str + (repeat_count * current_str)  # Expand substring
            else:
                current_str += char  # Append character to the current substring

        return current_str
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends