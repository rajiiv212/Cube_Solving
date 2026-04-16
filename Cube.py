import kociemba

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



import kociemba

# Map color names to cube notation
color_to_letter = {
    "white": "U",
    "red": "R",
    "skyblue": "F",
    "yellow": "D",
    "orange": "L",
    "green": "B"
}

def get_cube_input_colors():
    print("Enter your cube colors face by face.")
    print("Faces order: Up, Right, Front, Down, Left, Back")
    print("Colors: white, red, blue, yellow, orange, green")
    
    faces = ["Up", "Right", "Front", "Down", "Left", "Back"]
    cube_state = ""
    
    for face in faces:
        while True:
            face_input = input(f"{face} face (9 colors separated by space): ").strip().lower().split()
            if len(face_input) == 9 and all(c in color_to_letter for c in face_input):
                cube_state += "".join(color_to_letter[c] for c in face_input)
                break
            else:
                print("Invalid input! Enter exactly 9 colors from the list.")
    
    return cube_state

def main():
    cube_state = get_cube_input_colors()
    
    try:
        solution = kociemba.solve(cube_state)
        print("\nSolution to solve the cube:")
        print(solution)
    except Exception as e:
        print("Error solving cube:", e)

if __name__ == "__main__":
    main()
