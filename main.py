import streamlit as st



st.title("Rubik’s Cube Simulator")

st.markdown("This is a simple Rubik’s Cube simulator built with Python.")


colors = ["white", "yellow", "red", "orange", "skyblue", "green"]

cols = st.columns(6)

for col, color in zip(cols, colors):
    col.markdown(
        f"""
        <div style="
            width:100px;
            height:60px;
            background-color:{color};
            border-radius:8px;
            border:2px solid black;
        "></div>
        """,
        unsafe_allow_html=True
    )

st.markdown("")
st.markdown("")
st.markdown("")
# Function to create a 3x3 face with cube gaps
def face(color):
    st.markdown(
        f"""<div style=" display:flex; flex-direction:column; gap:2px; "> """ + "".join([
        f'<div style="display:flex; gap:1px;">' +
        "".join([f'<div style="width:35px; height:35px; background-color:{color}; border:1px solid black; border-radius:4px;"></div>' for _ in range(3)]) + '</div>' for _ in range(3)]) + "</div>",        unsafe_allow_html=True )

# --- Top face (U) exactly above "Front" ---
cols = st.columns([1,1,1,1,1,1])
with cols[1]:  # aligns with Front
    face("white")

cols = st.columns(6)
with cols[0]:
    st.markdown('<div style="display:flex; gap:3px;">', unsafe_allow_html=True)
    face("orange")  # Left
with cols[1]:
    st.markdown('<div style="margin-left:-11px;">', unsafe_allow_html=True)
    face("green")   # Front
with cols[2]:
    st.markdown('<div style="margin-left:1px;">', unsafe_allow_html=True)
    face("red")     # Right
with cols[3]:
    st.markdown('<div style="margin-left:1px;">', unsafe_allow_html=True)
    face("skyblue")    # Back

st.markdown('<div style="display:flex; gap:3px;">', unsafe_allow_html=True)
# --- Bottom face (D) exactly below "Front" ---
cols = st.columns([1,1,1,1,1,1])
with cols[1]:
    face("yellow")