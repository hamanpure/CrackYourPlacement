//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int findMinCycle(int V, vector<vector<int>>& edges) {
        const int INF = INT_MAX / 2;  // To prevent overflow
        vector<vector<int>> dist(V, vector<int>(V, INF));

        // Initialize distance matrix
        for (int i = 0; i < V; i++) {
            dist[i][i] = 0;
        }

        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            dist[u][v] = min(dist[u][v], w);
            dist[v][u] = min(dist[v][u], w);
        }

        int minCycle = INF;

        // Try removing each edge and compute shortest path
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];

            // Make a temp copy of distance matrix
            vector<vector<int>> temp = dist;
            temp[u][v] = temp[v][u] = INF;

            // Floyd-Warshall
            for (int k = 0; k < V; k++) {
                for (int i = 0; i < V; i++) {
                    for (int j = 0; j < V; j++) {
                        if (temp[i][k] < INF && temp[k][j] < INF) {
                            temp[i][j] = min(temp[i][j], temp[i][k] + temp[k][j]);
                        }
                    }
                }
            }

            if (temp[u][v] < INF) {
                minCycle = min(minCycle, temp[u][v] + w);
            }
        }

        return minCycle == INF ? -1 : minCycle;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;
        vector<vector<int>> edges;
        int i = 0;
        while (i++ < E) {
            int u, v, w;
            cin >> u >> v >> w;
            edges.push_back({u, v, w});
            edges.push_back({v, u, w});
        }

        Solution obj;
        int res = obj.findMinCycle(V, edges);

        cout << res << endl;
    }

    return 0;
}
// } Driver Code Ends