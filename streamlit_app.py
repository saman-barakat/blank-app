import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
col1, col2 = st.columns(2)
with col1:
    if st.button("Go to Info Page"):
        st.switch_page("Info")
with col2:
    if st.button("Go to Movies Page"):
        st.switch_page("Movies")