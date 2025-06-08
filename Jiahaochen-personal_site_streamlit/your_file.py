import streamlit as st
import os

# 定义加载本地 CSS 文件的函数
def local_css(file_name): 
    with open(file_name) as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

# 使用绝对路径加载 CSS 文件
base_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(base_dir, "static", "css", "style.css")
local_css(css_path)