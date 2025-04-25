import random

def is_valid(perm):
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if abs(perm[i] - perm[j]) == abs(i - j):
                return False
    return True

def find_random_solution():
    while True:
        perm = list(range(8))
        random.shuffle(perm)
        if is_valid(perm):
            return perm

def print_board(solution):
    for row in range(8):
        line = ""
        for col in range(8):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

solution = find_random_solution()
print_board(solution)
