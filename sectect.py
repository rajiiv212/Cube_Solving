import streamlit as st 
st.set_page_config(page_title="Rubik’s Cube Simulator") 
st.title("Rubik’s Cube Simulator") 
st.markdown("This is a simple Rubik’s Cube simulator built with Python.") 
colors = ["white", "yellow", "red", "orange", "skyblue", "green"] 
color_codes = { "white": "#FFFFFF", "yellow": "#FFFF00", "red": "#FF0000", "orange": "#FFA500", "skyblue": "#87CEEB", "green": "#008000" } 
# ------------------------- # SESSION STATE # ------------------------- 
if "clicked_color" not in st.session_state: 
    st.session_state.clicked_color = None 
    if "face" not in st.session_state: 
        st.session_state.face = ["lightgray"] * 9 
        st.session_state.face[4] = "white" 
# ------------------------- # COLOR BUTTONS CLASS # ------------------------- 
class ColorButtons: 
    def __init__(self): 
        self.colors = { 
            "Skyblue": "group1-a", 
            "Green": "group2-b", 
            "Orange": "group3-c", 
            "White": "group4-d", 
            "Yellow": "group5-e", 
            "Red": "group6-f" } 
        self.apply_css() 
        self.show_buttons() 
        self.show_result() 
        def apply_css(self): 
            CSS = """ 
            div[class*="st-key-group1"] 
            button {background-color:skyblue;width:100px;height:40px;border:2px solid black;} 
            
            div[class*="st-key-group2"] button {background-color:green;width:100px;height:40px;border:2px solid black;} 
            div[class*="st-key-group3"] button {background-color:orange;width:100px;height:40px;border:2px solid black;} 
            div[class*="st-key-group4"] button {background-color:white;width:100px;height:40px;border:2px solid black;} 
            div[class*="st-key-group5"] button {background-color:yellow;width:100px;height:40px;border:2px solid black;} 
            div[class*="st-key-group6"] button {background-color:red;width:100px;height:40px;border:2px solid black;} """ 
            st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True) 
        def show_buttons(self): 
            cols = st.columns(len(self.colors)) 
            for i, (color, key) in enumerate(self.colors.items()): 
                with cols[i]: 
                    if st.button(color, key=key): 
                        st.session_state.clicked_color = color.lower() 
        def show_result(self): 
            if st.session_state.clicked_color: 
                st.markdown(f"Selected color: **{st.session_state.clicked_color}**") 
    app = ColorButtons() 
# ------------------------- # GRID COLOR APPLY # -------------------------  
    def next_color(selected): 
        if selected is None: 
            return "lightgray" 
            return selected cols = st.columns(3) 
            for i in range(9): with cols[i % 3]: 
                if st.button(" ", key=f"cell_{i}") and i != 4: # 
                if st.button(" ", key=f"cell_{i}"): 
                    st.session_state.face[i] = next_color( st.session_state.clicked_color ) 
            CSS = """ 
            div[class*="st-key-cell_{i}"] 
            button { width:40px; height:40px; background-color:{st.session_state.face[i]}; 
            border:2px solid black; border-radius:4px; margin-top:-35px;} "> </div> """ 
        st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True) 
        st.write("Stored face:") 
        st.write(" ".join(st.session_state.face)

CSS = f"""
div[class*="st-key-cell_{i}"] button {{
width:40px;
height:40px;
background-color:{st.session_state.face[i]};
border:2px solid black;
border-radius:4px;
margin-top:-35px;
}}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)