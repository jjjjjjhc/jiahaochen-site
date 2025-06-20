import streamlit as st
import os, glob

path = os.getcwd().replace("\\", "/")

def load_css():
    """Load custom CSS from the static/css directory"""
    # Get the path to the CSS file
    css_file = os.path.join("static", "css", "style.css") #path+"/css/style.css"
    # Check if the file exists
    st.write(glob.glob("*"))
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_file}")
        
def apply_custom_css():
    """Apply custom CSS styles directly"""
    st.markdown("""
    <style>
    @import url('css/style.css');
    </style>
    """, unsafe_allow_html=True)
