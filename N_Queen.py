package aicode;
import java.util.*;

public class Test {
	static int n=4;
	static char[][] board=new char[4][4];
	static HashSet<Integer> col=new HashSet<Integer>();
	static HashSet<Integer> pdia=new HashSet<Integer>();
	static HashSet<Integer> ndia=new HashSet<Integer>();
	public static void main(String[] args) {
		for (int i = 0; i < n;i++) {
			for (int j = 0; j < n; j++) {
				board[i][j]='-';
			}
		}
		
		solve(0);
		
		
	}
	public static void display() {
		for (char[] cs : board) {
			for (char c : cs) {
				System.out.print(c+" ");
			}
			System.out.println();
		}
		System.out.println("================");
	}
	public static void solve(int row) {
		 	if(row==n) {
		 		display();
		 		return;
		 	}
		 	for (int c = 0; c <n ; c++) {
				if(col.contains(c)||pdia.contains(c+row)||ndia.contains(row-c)) {
					continue;
				}
				col.add(c);
				pdia.add(row+c);
				ndia.add(row-c);
				board[row][c]='Q';
				solve(row+1);
				col.remove(c);
				pdia.remove(row+c);
				ndia.remove(row-c);
				board[row][c]='-';
			}
	}

}
