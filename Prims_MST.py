import java.util.*;

public class PrimEasy {

    public static void main(String[] args) {

        int INF = 9999;

        int[][] graph = {
                {0, 2, 0, 6, 0},
                {2, 0, 3, 8, 5},
                {0, 3, 0, 0, 7},
                {6, 8, 0, 0, 9},
                {0, 5, 7, 9, 0}
        };

        int n = graph.length;

        boolean[] vis = new boolean[n];

        vis[0] = true;

        int edges = 0;

        int cost = 0;

        System.out.println("Edges:");

        while (edges < n - 1) {

            int min = INF;

            int u = -1;
            int v = -1;

            for (int i = 0; i < n; i++) {

                if (vis[i]) {

                    for (int j = 0; j < n; j++) {

                        if (!vis[j] &&
                                graph[i][j] != 0 &&
                                graph[i][j] < min) {

                            min = graph[i][j];

                            u = i;
                            v = j;
                        }

                    }

                }

            }

            System.out.println(u + " - " + v + " = " + min);

            vis[v] = true;

            cost += min;

            edges++;

        }

        System.out.println("Total Cost = " + cost);

    }
}
