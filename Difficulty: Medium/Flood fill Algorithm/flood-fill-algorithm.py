class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        # If the original color is the same as newColor, no change needed
        if original_color == newColor:
            return image

        def dfs(r, c):
            # Check boundaries and if the pixel is of original color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            # Change color
            image[r][c] = newColor
            # Recurse in 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends