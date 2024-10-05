import streamlit as st
from streamlit_elements import elements, mui, html, sync

# Add background image
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://www.icegif.com/wp-content/uploads/2023/04/icegif-771.gif');
            background-size: cover;
            background-position: tile;
            background-attachment: fixed;
        }
            
        h1 {
            color: #ffffff;
            text-decoration: underline;
            text-align: left;
            
        }
    </style>
""", unsafe_allow_html=True)

st.write("# Welcome to NASA Sustainable Development Goals Project")
st.subheader("NASA's Sustainable Development Goals (SDG) program focuses on using space technology and research to help solve important global challenges. The United Nations created 17 SDGs to make the world a better place by 2030. These goals include fighting climate change, protecting life on land and water, ensuring clean energy, and promoting education for all. NASA helps by using satellites to monitor Earth's environment, studying natural resources, and providing data that helps countries meet their SDG targets. The program shows how space science can make life better on Earth for everyone.")   # below the heading






st.latex(r''' powered by ASK-AI ''')  # small info at the bottom
