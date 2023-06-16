# pip install streamlit
# streamlit hello
# ctrl + c : 실행 종료 (터미널)

import streamlit as st  # streamlit -> import (가져오기) -> as (st 이름)
# st라는 변수명으로 streamlit의 기능들을 사용하겠다

# st. -> ctrl + space -> 다양한 기능(함수, 메소드)을 가지고 있다

st.title("Streamlit 이용 웹페이지")
st.header("Day 8")
st.subheader("기능에 대해서 배우는 중")
st.write("sdff")

# 기능이 실행되는 순서대로 화면에서 표현
st.video("https://www.youtube.cozm/watch?v=54vt4Nalaa8&list=PLwQjvFya6lZIasjkCXGjcLar6EvI_V6nm&index=2")  # 유튜브 링크
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
st.image("https://i.imgur.com/jorp5JH.png")  # 인터넷 링크
# 여러 가지 옵션을 넣어서 세부 기능들을 차이
st.image("img/image1.jpg")  # 파일 경로 (app.py)
st.image(image="img/image1.jpg")  # 키워드를 사용해서...
st.image("img/image1.jpg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/image1.jpg", width=100)  # 파일 경로 (app.py)

# 제목 마크다운
st.write("""
# 가장 큰 제목 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어ㅋ.
""")

# 서식
text = """
엔터 두번은 줄바꿈.

기울임 : *별표*를 하나씩 써주면 (별표대신) __언더바__

진하게(bold) : **별표**를 두개씩 써주면 ___언더바___

기울임 + 진하게(bold) : ***별표***를 세개씩 써주면 ____언더바____

취소선 : ~물결표~

"""


# https://imgur.com/
# streamlit run app.py