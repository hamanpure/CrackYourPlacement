class Solution:
    def startStation(self, gas, cost):
        # Your code here
        total_gas = sum(gas)
        total_cost = sum(cost)
    
        if total_gas < total_cost:
            return -1  # Not enough gas to complete the journey
    
        start = 0
        tank = 0  # Tracks remaining gas
    
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
    
            if tank < 0:  # Can't reach the next station
                start = i + 1  # Change starting station
                tank = 0  # Reset tank
    
        return start


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends