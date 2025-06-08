import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Jia Haochen</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        1-2/F Cheng Yu Tung Building, Ma Liu Shui,New Territories, Hong Kong <br>
        <a href="mailto:jiahaochen2000m@163.com">jiahaochen2000m.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I graduated from graduate school majoring in marketing, with solid and comprehensive basic theories and knowledge system of marketing and product operation.

        I have studied and researched the current situation and development direction of marketing in many industries, especially in the field of Internet products and information technology product marketing, I have strong interest, a deeper understanding and prospective research, a keen sense of the market and the ability to make decisive judgments.

        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, TensorFlow
        - Database: SQL
        - Data Visualization: Tableau, Power BI
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Communication: Presentation Skills, Business Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 