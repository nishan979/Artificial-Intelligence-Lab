class N_Queen:
    def __init__(self, a):
        self.N = a

    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(f"{board[i][j]} ", end='')
            print()

    def isSafe(self, grid, row, col):
        # Check this row on the left side
        for i in range(col):
            if grid[row][i] == 1:
                return False

        # Check upper diagonal on left side
        i, j = row, col
        while i >= 0 and j >= 0:
            if grid[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check lower diagonal on left side
        i, j = row, col
        while j >= 0 and i < self.N:
            if grid[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solveNQUtil(self, grid, col):
        if col >= self.N:
            return True

        for i in range(self.N):
            if self.isSafe(grid, i, col):
                grid[i][col] = 1

                if self.solveNQUtil(grid, col + 1):
                    return True

                grid[i][col] = 0  # BACKTRACK

        return False

    def solveNQ(self):
        grid = [[0 for _ in range(self.N)] for _ in range(self.N)]

        if not self.solveNQUtil(grid, 0):
            print(f"Solution does not exist for {self.N} queens.")
            return False

        print(f"Solution found for {self.N} queens:")
        self.printSolution(grid)
        return True


if __name__ == "__main__":
    n = int(input("Number of queens to place: "))
    queen_solver = N_Queen(n)
    queen_solver.solveNQ()
