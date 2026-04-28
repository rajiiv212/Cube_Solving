import random
import kociemba
from collections import Counter

colors = ["white", "red", "skyblue", "yellow", "orange", "green"]

fixed_positions = {
    4: "white",
    13: "red",
    22: "green",
    31: "yellow",
    40: "orange",
    49: "skyblue"
}

color_to_letter = {
    "white": "U",
    "red": "R",
    "skyblue": "B",
    "yellow": "D",
    "orange": "L",
    "green": "F"
}

first = ['red', 'green', 'red', 'yellow', 'white', 'white', 'white', 'yellow', 'orange', 'skyblue', 'green', 'skyblue', 'skyblue', 'red', 'orange', 'white', 'white', 'yellow', 'green', 'red', 'white', 'green', 'green', 'red', 'orange', 'orange', 'green', 'yellow', 'yellow', 'red', 'yellow', 'yellow', 'skyblue', 'red', 'white', 'green', 'skyblue', 'skyblue', 'orange', 'orange', 'orange', 'red', 'green', 'green', 'skyblue', 'white', 'orange', 'yellow',('white'), ('skyblue'), ('skyblue'), ('orange'), ('red'), ('yellow')]

def generate_cube():
    while True:
        # Step 1: create empty cube
        random_colors = [None] * 54

        # Step 2: fixed positions
        for pos, color in fixed_positions.items():
            random_colors[pos] = color

        # Step 3: limit 9 each
        color_counts = {color: 9 for color in colors}
        for color in fixed_positions.values():
            color_counts[color] -= 1

        remaining_colors = []
        for color, count in color_counts.items():
            remaining_colors.extend([color] * count)

        random.shuffle(remaining_colors)

        idx = 0
        for i in range(54):
            if random_colors[i] is None:
                random_colors[i] = remaining_colors[idx]
                idx += 1

        # Step 4: convert to cube string
        cube_state = "".join(color_to_letter[c] for c in first)

        # Step 5: try solving
        try:
            print("Generated a valid cube!",cube_state) 
            solution = kociemba.solve(cube_state)
            return random_colors, cube_state, solution

        except Exception:
            # invalid cube → retry
            continue


# Run until valid
random_colors, cube_state, solution = generate_cube()

print("Final Color List:")
print(random_colors)

print("\nCube State:")
print(cube_state)

print("\nSolution:")
print(solution)

# data = """RBRDUUUDLFBFFRLUUDBRUBBRLLBDDRDDFRUBFFLLLRBBFULDUFFLRD
# FRFFULUURLRDBRULUDULRLBDFFBBRBBDRULFDBFDLDDDFBLUUFBRLR
# UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"""

# data = data.replace("\n", "")  # join all lines into one string

# for i, ch in enumerate(data, start=1):
    # print(i, "is", ch)