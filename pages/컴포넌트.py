import streamlit as st

st.title("컴포넌트")
# 위-아래로 한 줄로만....
st.write("👨🏿‍🔬")
cols = st.columns(2)  # 컬럼 리스트
cols[0].write("👨🏿‍🔬")
cols[1].write("👨🏿‍🔬")
cols = st.columns(3)
# 🐦 -> n등분 -> 3등분
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
cols = cols[0].columns(3)
# 열의 열인 거임
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
