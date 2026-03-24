# import kociemba

# # Example cube state
# # Each face is represented by 9 characters in the order: Up, Right, Front, Down, Left, Back
# # Colors: U=Up, R=Right, F=Front, D=Down, L=Left, B=Back
# cube_state = (
#     "UUUUUUUUU"  # Up face
#     "RRRRRRRRR"  # Right face
#     "FFFFFFFFF"  # Front face
#     "DDDDDDDDD"  # Down face
#     "LLLLLLLLL"  # Left face
#     "BBBBBBBBB"  # Back face
# )

# try:
#     solution = kociemba.solve(cube_state)
#     print("Solution to solve the cube:")
#     print(solution)
# except Exception as e:
#     print("Error solving cube:", e)



from rubik_solver import utils

# Map color names to cube notation (Standard Kociemba: U=Up, R=Right, F=Front, D=Down, L=Left, B=Back)
color_to_letter = {
    "white": "U",
    "red": "R",
    "green": "F",
    "yellow": "D",
    "orange": "L",
    "skyblue": "B"
}

def solve_cube(cube_state):
    try:
        solution = utils.solve(cube_state, 'Kociemba')
        return " ".join(str(move) for move in solution)
    except Exception as e:
        return f"Error solving cube: {e}"

if __name__ == "__main__":
    # Test state
    test_state = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
    print("Solution:", solve_cube(test_state))

