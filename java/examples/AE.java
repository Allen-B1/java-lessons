import java.util.Scanner;

public class AE {
	public static void main(String[] args) {
		char[][] grid = {
			{' ', ' ', ' '},
			{' ', ' ', ' '},
			{' ', ' ', ' '},
		};

		Scanner sc = new Scanner(System.in);

		char turn = 'X';
		while (true) {
			// Make move
			System.out.println(turn + "'s turn");
			System.out.print("row [1-3]:");
			final int row = sc.nextInt() - 1;
			System.out.print("col [1-3]:");
			final int col = sc.nextInt() - 1;
			if (grid[row][col] != ' ') {
				System.out.println("not empty");
				continue;
			}
			grid[row][col] = turn;

			// Display tic-tac-toe board
			for (char[] rowe: grid) {
				for (char cell: rowe) {
					System.out.print("|" + cell);
				}
				System.out.println("|");
			}

			// Win condition
			boolean won = false;
			for (int i = 0; i < 3; i++) {
				if ((grid[0][i] == grid[1][i] && grid[1][i] == grid[2][i] && grid[2][i] == turn)
					|| (grid[i][0] == grid[i][1] && grid[i][1] == grid[i][2] && grid[i][2] == turn)) {
					won = true;
				}
			}
			if ((grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2] && grid[2][2] == turn) ||
				(grid[2][0] == grid[1][1] && grid[1][1] == grid[0][2] && grid[1][1] == turn)) {
				won = true;
			}
			if (won) {
				System.out.println(turn + " won!");
				break;
			}

			// Switch turn
			if (turn == 'X') turn = 'O';
			else turn = 'X';
		}
	}
}