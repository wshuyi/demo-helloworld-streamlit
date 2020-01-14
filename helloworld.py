import streamlit as st
import numpy as np
import pandas as pd

st.title("my first app")

@st.cache
def load_data():
    df = pd.read_csv("data.csv")
    df = df[['EVENT_TYPE', 'CREATE_TIME', 'COUNTY', 'LAT', 'LON']]
    df.columns = ['event_type', 'time', 'county', 'lat', 'lon']
    return df

df = load_data()

st.table(df.head())

event_list = df["event_type"].unique()

event_type = st.sidebar.selectbox(
    "Which kind of event do you want to explore?",
    event_list
)

county_list = df["county"].unique()

county_name = st.sidebar.selectbox(
    "Which county?",
    county_list
) 

part_df = df[(df["event_type"]==event_type) & (df['county']==county_name)]

st.write(f"根据你的筛选，数据包含{len(part_df)}行")

st.map(part_df)

st.markdown("""
欢迎订阅我的微信公众号“玉树芝兰”，**第一时间免费**收到文章更新。别忘了**加星标**，以免错过新推送提示。

![](https://tva1.sinaimg.cn/large/006tNbRwly1gavw3v4iagj3076076dg2.jpg)

赞赏就是力量。

![](https://tva1.sinaimg.cn/large/006tNbRwly1gavw3vhpnpj30b40b4jrs.jpg)

如果你对 Python 与数据科学感兴趣，希望能与其他热爱学习的小伙伴一起讨论切磋，答疑解惑，欢迎加入知识星球。

![](https://tva1.sinaimg.cn/large/006tNbRwly1gavw3vz0ahj30dc0hzdgc.jpg)
""")