import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# st.write('Hello world!')
# st.write 命令被用作显示文字消息

# 标题
st.header('st.button')

# 如果点击了按钮 则显示Why hello there
# 否则显示Goodbye
#  st.button() 语句接收了一个值为 Say hello 的 label 参数，会作为显示在按钮上的文字
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.header('st.write')

# 基本用法就是现实文字和使用 Markdown 语法的文本 
# *斜体*  :表情:
st.write('Hello,*World!*:sunglasses:')
# 输出数字
st.write(1234)
# 输出 pandas DataFrame，将数据框显示为表格
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.write(df)
# sample 4，多个参数
st.write('Below is a DataFrame:',df,'Above is a DataFrame.')
# sample 5 显示图标
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b' , size = 'c',tooltip = ['a','b','c']
)
st.write(c)