import streamlit as st
import pandas as pd
import numpy as np


#text를 입력하는 검색창을 하나 만든다
#ani_list에 있는 글자가 일부라도 들어가면
#image_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어주세요
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


word = st.text_input('입력: ')
st.write(word)
print(word)
for i in word:
    if i in ani_list[0]:
        st.image(img_list[0])
    elif i in ani_list[1]:
        st.image(img_list[1])
    elif i in ani_list[2]:
        st.image(img_list[2])

"""
for ani in ani_list:
    if word in ani:
        img_idx = ani_list.index(word)

st.image(img_list[img_idx])
"""