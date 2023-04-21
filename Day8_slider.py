import streamlit as st
from datetime import time,datetime
import pandas as pd
import numpy as np

st.header('st.slider')

# sample 1
st.subheader('Slider')

age = st.slider('How old are you?',0,130,25)
st.write("I'm ",age,'years old')

# # 如你所见，st.slider() 命令被用作收集用户输入的年龄信息。
# 第一个参数为 滑条 组件上方的标题文字，此处为询问用户年龄：'How old are you?'。
# 接下来三个整数 0, 130, 25 分别代表最小值、最大值和默认数值。


# sample 2
st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0,100.0,(25.0,75.0)
)
st.write(values)

# 范围滑条允许同时输入一对下界与上界数值。
# 第一个参数为 范围滑条 组件上方的标题文字，此处为询问数字范围：'Select a range of values'。
# 接下来三个参数 0.0, 100.0, (25.0, 75.0) 分别代表了最小值、最大值和默认的一对下界与上界数值 (25.0, 75.0) 。

# sample 3
st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value = (time(11,30),time(14,45))
)
st.write("You're scheduled for:",appointment)
# 时间范围滑条允许同时输入一对下界与上界时间。
# 第一个参数为 时间范围滑条 组件上方的标题文字，此处为询问预约时段：'Schedule your appointment:'。
# 这里下界与上界时间的默认值分别被设为 11:30 和 14:45。

# sample 4
st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY - hh:mm"
)
st.write("Start time:",start_time)
# 日期时间滑条允许输入一个日期时间。
# 第一个参数为 日期时间滑条 组件上方的标题文字，此处为询问开始时间：'When do you start?'。
# 这里日期时间的默认值通过 value 参数被设为 2020 年 1 月 1 日 9:30。

# 折线图
st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.write(chart_data)
st.line_chart(chart_data)