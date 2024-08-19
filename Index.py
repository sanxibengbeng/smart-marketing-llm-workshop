import streamlit as st

st.set_page_config(
    page_title="Workshop Index",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)
# 读取 README.md 文件内容
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()
    # 在 Streamlit 应用程序中显示 README.md 内容
    st.markdown(readme_content)