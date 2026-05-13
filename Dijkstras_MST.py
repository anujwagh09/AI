import java.util.*;

public class DijkstraEasy {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int INF = 9999;

        System.out.println("Enter number of nodes:");
        int n = sc.nextInt();

        int[][] graph = new int[n][n];

        System.out.println("Enter adjacency matrix:");

        for (int i = 0; i < n; i++) {

            for (int j = 0; j < n; j++) {

                graph[i][j] = sc.nextInt();

                if (graph[i][j] == -1) {
                    graph[i][j] = INF;
                }

            }

        }

        int[] dist = new int[n];
        boolean[] vis = new boolean[n];

        Arrays.fill(dist, INF);

        dist[0] = 0;

        for (int i = 0; i < n; i++) {

            int min = INF;
            int u = -1;

            // find nearest node
            for (int j = 0; j < n; j++) {

                if (!vis[j] && dist[j] < min) {
                    min = dist[j];
                    u = j;
                }

            }

            vis[u] = true;

            
            for (int v = 0; v < n; v++) {

                if (!vis[v] &&
                        graph[u][v] != INF &&
                        dist[u] + graph[u][v] < dist[v]) {

                    dist[v] = dist[u] + graph[u][v];

                }

            }

        }

        System.out.println("Shortest Distances:");

        for (int i = 0; i < n; i++) {
            System.out.println(i + " -> " + dist[i]);
        }

    }
}
