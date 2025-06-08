import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="贾浩辰0220.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Jia Haochen")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** jiahaochen2000m@163.com
    - **Phone:** +86 136-4234-4176
    - **WeChat:** JHC-GEOFF
    - **LinkedIn:** [linkedin.com/in/Haochen-Jia](https://linkedin.com/in/Haochen-Jia)
    - **Address:**  YulongSt, Longhua District, Shenzhen, China
    """)

    st.header("Professional Summary")
    st.markdown("""
    Multi-terminal e-commerce related experience with the ability to perform e-commerce operations related tasks, as well as a degree of marketing knowledge.
    """)

    st.header("Work Experience")
    st.markdown("""
    **New Business Operations Inter, ByteDance Ltd.**
    - *October 2024 – February 2025*
    - New Merchants Merchant Card Start-up Program: In order to facilitate new merchants in the shelf field to achieve turnover transformation, to participate in the development of merchant card start-up strategy, through the research of competing support strategies, to understand the merchant side of the business pain points, to develop a four-stage merchant card operation is divided into good products, experience points, newbie village, marketing acceleration. Through researching the support strategies of competitors and understanding the pain points of the merchant side of the business, we have formulated the four phases of merchant card operation, which are divided into doing a good job in merchandise, experience points, novice village and marketing acceleration. Completing the merchant card volume start-up novice manual, and docking the merchant learning center to complete the course production, through the merchant group, live broadcast and other ways of publicity, docking the merchant for one-on-one analysis of the Q&A, covering a total of 100 + merchants, 30 days out of the camp rate of 39.4%, a single merchant weekly GMV 1k → 3w.
    - Experience points strategy: Participate in the optimization of merchant store experience points strategy, according to the logistics experience, service experience, product experience weighted calculation, analysis of the merchant side in the experience points out of the points stage of the card point, the development of 0-10 single and 10-30 single fast out of the points of the novice rights and interests and paths, and to complete the follow-up experience points optimization strategy. 30 days to help merchants to achieve the experience points out of the points of the time to shorten the time by 20%, for the subsequent investment promotion. Lay the foundation for the subsequent investment.
    - Merchant Operation: Responsible for following up with high potential merchants to quickly reach 10W+, which is independently responsible for docking the flagship store of Summa Lingerie, by analyzing its business data, formulating the strategy of short-video testing + live broadcasting to hit the explosion, and using the public domain and marketing tools to help it complete the flagship store 1.0 landing.

    **Data Operations Intern, SF-Express Technology Co. **
    - *October 2023 – July 2024*
    - Responsible for supervising the quality of production work of new outsourcing vendors, collecting daily work content, comparing with the original outsourcing data, writing daily reports, and answering questions about new outsourcing on a daily basis. After half a month of inspection, the accuracy of POI address conformity and completeness of work has increased from 60% to more than 95% from the very beginning. Introduced new suppliers for the company and shared the operation pressure.
    - Optimized the original operation process in the building completion project, analyzed the operation process, total volume and time through the first-view video of the operator's operation, formulated corresponding plans to improve the system and increase efficiency, and continuously collected questions and feedback, so that the final operation tasks were completed within 5 working days from 5.5 working days under the premise of guaranteeing the accuracy of the tasks.
    - Monitor the daily data, use the Excel table form to screen out the data to do comparison, record the daily capacity of each region and the problems encountered, abnormalities in a timely manner to the leadership to report processing.
    -Actively communicate with the product side based on business requirements and discuss together to achieve common goals.
    """)

    st.header("Education")
    st.markdown("""
    **Master Of Science in Marketing**
    - Chinese University of Hong Kong
    - *Graduated: November 2025*
    - GPA: 3.4/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R
    - **Databases:** MySQL
    - **Tools:** Word, PPT, Excel
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Projects")
    st.markdown("""
    **999 Dermatropin Marketing Program**
    - Project Background:999 Dermatophores has remarkable efficacy, high brand awareness, and good market performance, but faces challenges such as fierce competition in social media, strict regulation of OTC drugs, brand aging, and consumers' concerns about the product's ingredients (e.g., hormones), etc. By analyzing the consumers' needs through big data, we can provide a marketing plan and set up a social media communication matrix to realize the rejuvenation of the brand.
    - Data Insights:Responsible for coordinating data insights, analyzing target demographics and interest preferences through the use of social listening and focus group research methods. Analyzed a large number of posts using the keywords “dermatitis” and “eczema” and found that consumers are concerned about skin problems and have a strong interest in related health knowledge and products. Consumers who are concerned about skin problems are concentrated in coastal areas, mostly in Guangdong; 80% of the audience is under 24 years old and are interested in traveling, food, outdoor activities and health.
    """)
    st.header("Languages")
    st.markdown("""
    - **English:** Fluent
    - **Mandarin:** Native
    """)

    st.header("Interests")
    st.markdown("""
    - Movies and reading
    - Video game enthusiasts
    - Hiking and outdoor activities
    """)

    st.markdown("---")