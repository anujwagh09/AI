# N-Queens using Backtracking + Branch & Bound (Matrix Output)

def solve_nqueens(n):
    def print_solution(board):
        print("\nSolution:\n")
        for i in range(n):
            row = ['0'] * n
            row[board[i]] = '1'
            print(" ".join(row))

    def solve(row):
        if row == n:
            print_solution(board)
            return True

        for col in range(n):
            # Branch & Bound condition
            if not cols[col] and not diag1[row - col] and not diag2[row + col]:

                # Place queen
                board[row] = col
                cols[col] = diag1[row - col] = diag2[row + col] = True

                # Recur
                if solve(row + 1):
                    return True   # print only first solution

                # Backtrack
                cols[col] = diag1[row - col] = diag2[row + col] = False
                board[row] = -1

        return False

    board = [-1] * n
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    solve(0)


# -------- Main --------
n = int(input("Enter number of queens: "))
solve_nqueens(n)