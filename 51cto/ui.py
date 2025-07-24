import pandas as pd
import streamlit as st


#示例：数据可视化
# 上传 xlsx 文件
uploaded_file =st.file_uploader("上传数据",type='xlsx')
if uploaded_file:
    #读取Excel文件
    excel_file=pd.ExcelFile(uploaded_file)
    #获取第一个工作表的数据
    df=excel_file.parse(excel_file.sheet_names)

    #显示数据的前几行
    st.dataframe(df.head())

    #查找包含”销售数据“的列
    column_name=None
    for col in df.columns:
        if "销售数量" in  col:
            column_name=col
            break

    if column_name:
        # 生成“销售数量”列的折线图111
        st.line_chart(df[column_name])
    else:
        st.warning("数据中未找到包含 '销售数量' 的列，无法生成图表。")