import streamlit as st
import os

# 定义加载本地 CSS 文件的函数
def local_css(file_name): 
    with open(file_name) as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

# 输出当前工作目录
st.write("cwd:", os.getcwd()) 

# 使用当前工作目录构建 CSS 文件路径并加载 CSS
local_css(os.path.join(os.getcwd(), "static", "css", "style.css"))