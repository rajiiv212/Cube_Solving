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
        div[class*="st-key-group2"] button {background-color:green;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group3"] button {background-color:orange;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group4"] button {background-color:white;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group5"] button {background-color:yellow;width:90px;height:40px;border:2px solid black;}
        div[class*="st-key-group6"] button {background-color:red;width:90px;height:40px;border:2px solid black;}
        """
        st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    def show_buttons(self):
        cols = st.columns(len(self.colors))
        for i, (color, key) in enumerate(self.colors.items()):
            with cols[i]:
                if st.button(color, key=key):
                    st.session_state.clicked_color = color.lower()

    def show_result(self):
        if st.session_state.clicked_color:
            st.write("Selected color:", st.session_state.clicked_color)


ColorButtons()


# -------------------------
# FACE FUNCTION using CSS
# -------------------------
def face(face_name, center_color):
    if face_name not in st.session_state:
        st.session_state[face_name] = ["lightgray"] * 9
        st.session_state[face_name][4] = center_color  # center is fixed

    # create 3 columns per row
    cols = st.columns(3)

    for i in range(9):
        with cols[i % 3]:

            # button click (skip center)
            if st.button(" ", key=f"cell_{face_name}_{i}") and i != 4:
                if st.session_state.clicked_color:
                    st.session_state[face_name][i] = st.session_state.clicked_color

            # dynamic CSS for this button
            CSS = f"""
div[class*="st-key-cell_{face_name}_{i}"] button {{
    width:40px;
    height:40px;
    background-color:{st.session_state[face_name][i]};
    border:2px solid black;
    border-radius:4px;
    margin-top:0px;
}}
"""
            st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

    return " ".join(st.session_state[face_name])


# -------------------------
# CUBE LAYOUT
# -------------------------
st.markdown("")

cols = st.columns([1,1,1,1,1,1])
with cols[1]:
    up_face = face("up", "white")

st.markdown("")

cols = st.columns(6)
with cols[0]:
    left_face = face("left", "orange")
with cols[1]:
    front_face = face("front", "green")
with cols[2]:
    right_face = face("right", "red")
with cols[3]:
    back_face = face("back", "skyblue")

st.markdown("")
cols = st.columns([1,1,1,1,1,1])
with cols[1]:
    down_face = face("down", "yellow")

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