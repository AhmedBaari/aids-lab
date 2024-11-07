import math
import random

# Display the board in a readable format
def display(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))
    print()

# Fill empty cells in each row with random values that are not already in the row
def fill(board):
    for i in range(9):
        # Get numbers that can fill this row
        choices = list(set(range(1, 10)) - set(board[i]) - {0})
        random.shuffle(choices)  # Shuffle choices for randomness
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = choices.pop()  # Fill empty cell

# Calculate the number of conflicts (duplicate values in rows, columns, and 3x3 blocks)
def cost(board):
    conflicts = 0
    for n in range(9):
        # Check row and column conflicts
        conflicts += 9 - len(set(board[n]))  # Row conflicts # removes dups
        conflicts += 9 - len(set(board[j][n] for j in range(9)))  # Column conflicts
    # Check 3x3 block conflicts
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            block = [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
            conflicts += 9 - len(set(block))  # Block conflicts
    return conflicts

# Generate a new neighbor board by swapping two random values in a row
def next(board, fixed):
    neighbor = [row[:] for row in board]  # Copy board
    # choose a random row
    row = random.randint(0, 8)
    # Find swappable columns (not in fixed positions) in this row
    cols = [col for col in range(9) if (row, col) not in fixed]
    # ensure atleast 2 swappable positions
    if len(cols) >= 2:
        # randomly select 2 columns
        col1, col2 = random.sample(cols, 2)
        # swapping
        neighbor[row][col1], neighbor[row][col2] = neighbor[row][col2], neighbor[row][col1]
    return neighbor

# Solve the Sudoku using Simulated Annealing
def simulated_annealing(board, initial_temp=1.0, cooling_rate=0.99, min_temp=0.001):
    # Identify fixed positions (cells initially filled)
    fixed = [(x, y) for x in range(9) for y in range(9) if board[x][y] != 0]
    fill(board)  # Randomly fill board as starting point
    current = best = board  # Track best and current board
    temp = initial_temp  # Set initial temperature

    # Annealing loop
    while temp > min_temp:
        neighbor = next(current, fixed)
        delta = cost(neighbor) - cost(current)  # Calculate cost difference

        # Accept neighbor if it improves or by a probability if not
        if delta < 0 or random.random() < math.exp(-delta / temp): ##⭐
            current = neighbor
            if cost(current) < cost(best):  # Update best if current is better
                best = current

        temp *= cooling_rate  # Gradually reduce temperature

    print(f"Sudoku ({'Best Possible State | Conflicts = ' + str(cost(best)) if cost(best) else 'Solved'})")
    display(best)  # Display the final board

# Main function to run the solver
def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    simulated_annealing(board)

# Run the main function
main()
