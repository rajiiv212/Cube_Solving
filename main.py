import kociemba
import streamlit as st

st.set_page_config(page_title="Rubik’s Cube Simulator")
st.title("Rubik’s Cube Simulator")

st.markdown("Click a color, then click a square to fill it.")

colors = ["white", "yellow", "red", "orange", "skyblue", "green"]

# -------------------------
# SESSION STATE
# -------------------------
if "clicked_color" not in st.session_state:
    st.session_state.clicked_color = None


def is_color_full(target_color):
    if not target_color:
        return False
    count = 0
    faces = {"up": "white", "left": "orange", "front": "green", "right": "red", "back": "skyblue", "down": "yellow"}
    for f_name, f_center in faces.items():
        if f_name in st.session_state:
            count += st.session_state[f_name].count(target_color)
        else:
            if f_center == target_color:
                count += 1
    return count >= 9

# -------------------------
# COLOR BUTTONS
# -------------------------
class ColorButtons:
    def __init__(self):
        self.colors = {
            "Skyblue": "group1",
            "Green": "group2",
            "Orange": "group3",
            "White": "group4",
            "Yellow": "group5",
            "Red": "group6"
        }
        self.apply_css()
        self.show_buttons()
        self.show_result()

    def apply_css(self):
        CSS = """
        div[class*="st-key-group1"] button {background-color:skyblue;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group1"] button:disabled {opacity: 0.9;background-color:skyblue; border: 2px solid grey !important;}
        div[class*="st-key-group2"] button {background-color:green;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group2"] button:disabled {opacity: 0.9;background-color:green; border: 2px solid grey !important;}
        div[class*="st-key-group3"] button {background-color:orange;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group3"] button:disabled {opacity: 0.9;background-color:orange; border: 2px solid grey !important;}
        div[class*="st-key-group4"] button {background-color:white;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group4"] button:disabled {opacity: 0.9;background-color:white; border: 2px solid grey !important;}
        div[class*="st-key-group5"] button {background-color:yellow;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group5"] button:disabled {opacity: 0.9;background-color:yellow; border: 2px solid grey !important;}
        div[class*="st-key-group6"] button {background-color:red;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group6"] button:disabled {opacity: 0.9;background-color:red; border: 2px solid grey !important;}
        """
        st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    def show_buttons(self):
        cols = st.columns(len(self.colors))
        for i, (color, key) in enumerate(self.colors.items()):
            color_lower = color.lower()
            with cols[i]:
                # Automatically disable button if the color already has 9 squares on the cube
                if st.button(color, key=key, disabled=is_color_full(color_lower)):
                    st.session_state.clicked_color = color_lower

    def show_result(self):
        # We wrap the feedback messages in an invisible container with exactly 75px minimum height. 
        # This prevents the cube layout from jumping up and down when messages appear/disappear!
        with st.container():
            st.markdown("<div class='feedback-anchor'></div>", unsafe_allow_html=True)
            st.markdown("""
            <style>
            /* Apply 75px min-height to the specific vertical block holding our feedback anchor */
            div:has(> div[data-testid="stElementContainer"] .feedback-anchor),
            div:has(> div[data-testid="element-container"] .feedback-anchor) {
                min-height: 75px !important;
            }
            /* Hide the anchor itself to avoid extra spacing */
            div[data-testid="stElementContainer"]:has(.feedback-anchor), 
            div[data-testid="element-container"]:has(.feedback-anchor) {
                display: none !important;
                margin: 0 !important;
            }
            </style>
            """, unsafe_allow_html=True)

            if st.session_state.clicked_color:
                if st.session_state.clicked_color == "none":
                    pass
                elif is_color_full(st.session_state.clicked_color):
                    st.warning(f"**{st.session_state.clicked_color.capitalize()}** has reached the maximum of 9 squares!")
                    # Deselect active color because it's full
                    st.session_state.clicked_color = None
                else:
                    st.info(f"Selected color: **{st.session_state.clicked_color.capitalize()}**")

ColorButtons()


# -------------------------
# FACE FUNCTION using CSS
# -------------------------
def face(face_name, center_color):
    if face_name not in st.session_state:
        st.session_state[face_name] = ["lightgray"] * 9
        st.session_state[face_name][4] = center_color  # center is fixed

    # Draw 9 buttons sequentially; they will be arranged by CSS grid on their parent vertical block
    for i in range(9):
        # button click
        if st.button(" ", key=f"cell_{face_name}_{i}") and i != 4:
            if "clicked_color" in st.session_state and st.session_state.clicked_color:
                st.session_state[face_name][i] = st.session_state.clicked_color
                st.rerun()

    # Produce CSS rules for the exact colors and 3x3 grid uniform layout with 4px gap
    css_rules = []
    
    css_rules.append(f"""
        /* Target the vertical block holding this column's buttons and turn it into a CSS Grid */
        /* Checks for both "column" and "stColumn" depending on Streamlit version */
        div[data-testid="column"]:has(div[class*="st-key-cell_{face_name}_0"]) > div,
        div[data-testid="stColumn"]:has(div[class*="st-key-cell_{face_name}_0"]) > div {{
            display: grid !important;
            grid-template-columns: repeat(3, 40px) !important;
            grid-template-rows: repeat(3, 40px) !important;
            gap: 2px !important;
            width: max-content !important;
            justify-content: center !important;
            align-content: center !important;
        }}

        /* Hide the container for the injected <style> block so it doesn't break the 3x3 layout */
        div[data-testid="column"]:has(div[class*="st-key-cell_{face_name}_0"]) > div > div:not(:has(.stButton)),
        div[data-testid="stColumn"]:has(div[class*="st-key-cell_{face_name}_0"]) > div > div:not(:has(.stButton)) {{
            display: none !important;
        }}
    """)

    for i in range(9):
        color = st.session_state[face_name][i]
        css_rules.append(f"""
        div[class*="st-key-cell_{face_name}_{i}"] button {{
            background-color: {color} !important;
            width: 40px !important;
            height: 40px !important;
            min-height: 40px !important;
            margin: 0px !important;
            padding: 0px !important;
            border: 2px solid black !important;
            border-radius: 4px !important;
            display: block !important;
        }}
        """)
        
    st.markdown(f"<style>{''.join(css_rules)}</style>", unsafe_allow_html=True)

    return " ".join(st.session_state[face_name])


# -------------------------
# CUBE LAYOUT
# -------------------------
with st.container():
    st.markdown("<div class='cube-layout-marker'></div>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    /* 1) Vertical block holding the 3 horizontal rows of faces */
    div:has(> div[data-testid="stElementContainer"] .cube-layout-marker), 
    div:has(> div[data-testid="element-container"] .cube-layout-marker) {
        gap: 2px !important;
    }
    
    /* 2) Horizontal blocks (the rows holding the face columns) */
    div:has(> div[data-testid="stElementContainer"] .cube-layout-marker) div[data-testid="stHorizontalBlock"],
    div:has(> div[data-testid="element-container"] .cube-layout-marker) div[data-testid="stHorizontalBlock"] {
        gap: 2px !important;
        align-items: start !important;
    }

    /* 3) Adjust all columns within the cube layout to be perfectly 124px 
          This matches the 3x40px buttons + 2x2px gaps for each face.
          Forcing this width ensures perfect alignment for the empty slots! */
    div:has(> div[data-testid="stElementContainer"] .cube-layout-marker) div[data-testid="stColumn"],
    div:has(> div[data-testid="element-container"] .cube-layout-marker) div[data-testid="column"],
    div:has(> div[data-testid="stElementContainer"] .cube-layout-marker) div[data-testid="column"],
    div:has(> div[data-testid="element-container"] .cube-layout-marker) div[data-testid="stColumn"] {
        padding: 0px !important;
        min-width: 124px !important; 
        max-width: 124px !important;
        width: 124px !important;
        flex: none !important;
    }
    
    /* Hide marker wrapper */
    div[data-testid="stElementContainer"]:has(.cube-layout-marker), 
    div[data-testid="element-container"]:has(.cube-layout-marker) {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns([1,1,1,1,1,1])
    with cols[1]:
        up_face = face("up", "white")

    cols = st.columns(6)
    with cols[0]:
        left_face = face("left", "orange")
    with cols[1]:
        front_face = face("front", "green")
    with cols[2]:
        right_face = face("right", "red")
    with cols[3]:
        back_face = face("back", "skyblue")

    cols = st.columns([1,1,1,1,1,1])
    with cols[1]:
        down_face = face("down", "yellow")




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



# -------------------------
# SHOW STORED FACES
# -------------------------
st.write("Cube data:")
st.write("Up:", up_face)
st.write("Left:", left_face)
st.write("Front:", front_face)
st.write("Right:", right_face)
st.write("Back:", back_face)
st.write("Down:", down_face)

# -------------------------
# CUBE STATISTICS
# -------------------------
st.divider()
st.subheader("Cube Statistics")

# Convert the space-separated output strings back into lists of colors
up_list = up_face.split()
left_list = left_face.split()
front_list = front_face.split()
right_list = right_face.split()
back_list = back_face.split()
down_list = down_face.split()

# Combine all 54 squares to count the total of each color
all_squares = up_list + left_list + front_list + right_list + back_list + down_list

# Display the count of each color
st.write("**Total Colors Present:**")
# 'colors' is defined directly at the top of main.py
track_colors = colors + ["lightgray"]
count_cols = st.columns(len(track_colors))

for i, color in enumerate(track_colors):
    count = all_squares.count(color)
    with count_cols[i]:
        st.metric(label=color.capitalize(), value=count)

# Calculate how many squares currently match their fixed center color
solved_count = 0
solved_count += sum(1 for c in up_list if c == "white")
solved_count += sum(1 for c in left_list if c == "orange")
solved_count += sum(1 for c in front_list if c == "green")
solved_count += sum(1 for c in right_list if c == "red")
solved_count += sum(1 for c in back_list if c == "skyblue")
solved_count += sum(1 for c in down_list if c == "yellow")

st.write(f"**Solved squares:** {solved_count} / 54")


# -------------------------
# SOLVE CUBE (KOCIEMBA)
# -------------------------
st.divider()
st.subheader("Cube Solver")

import kociemba

def solve_from_gui():
    # Kociemba expects 54 characters in U R F D L B order!
    color_to_letter = {
        "white": "U",
        "red": "R",
        "skyblue": "F",
        "yellow": "D",
        "orange": "L",
        "green": "B"
    }
    
    # 1. Assemble the cube faces EXACTLY in U R F D L B order for the algorithm
    cube_sequence = up_list + right_list + front_list + down_list + left_list + back_list
    
    try:
        # 2. Map color names to letter notation
        cube_state = "".join(color_to_letter[c] for c in cube_sequence)
        
        # 3. Solve
        solution = kociemba.solve(cube_state)
        return "Success", solution
        
    except KeyError:
        return "Error", "Some squares are uncolored (lightgray) or invalid."
    except ValueError as e:
        return "Error", f"Invalid cube configuration: {e}"
    except Exception as e:
        return "Error", str(e)

if st.button("Solve Cube", type="primary", use_container_width=True):
    if solved_count == 54:
        st.success("The cube is already solved!")
    elif "lightgray" in all_squares:
        st.error("Cannot solve! There are still unpainted squares on the cube.")
    else:
        with st.spinner("Calculating optimal solution..."):
            status, msg = solve_from_gui()
            if status == "Error":
                st.error(msg)
            else:
                st.balloons()
                st.success("Algorithm Found!")
                st.code(msg, language="text")



