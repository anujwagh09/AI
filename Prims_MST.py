package aicode;

import java.util.*;

class Pair {
	int node;
	int weight;

	public Pair(int node, int weight) {
		super();
		this.node = node;
		this.weight = weight;
	}
}

public class Prim {
	static boolean[] visited;
	static ArrayList<Pair> []adj;

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number of Node :");
		int n=sc.nextInt();
		System.out.println("Enter number of Edge :");
		int e=sc.nextInt();
		
		adj = new ArrayList[n];
		visited=new boolean[n];
		
		for (int i = 0; i < n;i++) {
			adj[i]=new ArrayList<Pair>();
		}
		for (int i = 0; i < e; i++) {
			System.out.println("Enter  Node1 :");
			int u=sc.nextInt();
			System.out.println("Enter  Node2 :");
			int v=sc.nextInt();
			System.out.println("Enter  Weight :");
			int w=sc.nextInt();
			
			adj[u].add(new Pair(v, w));
			adj[v].add(new Pair(u, w));
			
			
		}
		PriorityQueue<Pair> pq=new PriorityQueue<Pair>((a,b)->a.weight-b.weight);
		pq.add(new Pair(0, 0));
		int cost=0;
		while (!pq.isEmpty()) {
			Pair current=pq.poll();
			int node=current.node;
			
			if(visited[node]) {
				continue;
			}
			visited[node]=true;
			
			cost+=current.weight;
			 
			for (Pair neb : adj[node]) {
				if(!visited[neb.node]) {
					pq.add(new Pair(neb.node, neb.weight));
				}
			}
			
			
		}
		System.out.println("MINI COST "+cost);
		
	}

}
