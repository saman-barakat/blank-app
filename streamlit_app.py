import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
col1, col2 = st.columns(2)
with col1:
    if st.button("Go to Page 1"):
        st.switch_page("pages/1_page1.py")
with col2:
    if st.button("Go to Page 2"):
        st.switch_page("pages/2_page2.py")