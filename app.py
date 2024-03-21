import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加載CSV文件
data = pd.read_csv('onlinefoods.csv')

# Streamlit應用
st.title('Online Food Dataset')

# 顯示數據
st.subheader('數據概覽')
st.write(data)
df = pd.DataFrame(data)
# Define a mapping from gender to emoji
gender_to_emoji = {
    'Male': '👨',
    'Female': '👩',
    # Add more mappings if there are more genders
}

# Create a new column 'Gender Emoji' by mapping the 'Gender' column using the defined mapping
data['Gender Emoji'] = data['Gender'].map(gender_to_emoji)

# Display the dataframe
st.dataframe(data)

# 創建一個新的列列表，去除不想要的欄位
columns_to_use = data.columns.drop(['latitude','longitude'])
# 選擇可視化列
viz_column = st.selectbox('選擇要可視化的列', columns_to_use)

# 根據選擇的列繪制圖表
if viz_column in data.select_dtypes(include=['int64', 'float64']).columns:
    st.subheader(f'{viz_column}分布')
    fig, ax = plt.subplots()
    ax = sns.histplot(data=data, x=viz_column, bins=20, color='#ffaa0088')
    st.pyplot(fig)
elif viz_column in data.select_dtypes(include=['object']).columns:
    st.subheader(f'{viz_column}分布')
    column_counts = data[viz_column].value_counts()
    fig, ax = plt.subplots()
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink'] 
    ax.pie(column_counts, labels=column_counts.index, autopct='%1.1f%%', colors = colors)
    ax.axis('equal')
    st.pyplot(fig)
# elif viz_column in data.select_dtypes(include=['object']).columns:
#     st.subheader(f'{viz_column}分類統計')
#     st.bar_chart(data[viz_column].value_counts(), color='#ffaa0088')
# 繪製地圖
if 'latitude' in data.columns and 'longitude' in data.columns:
    st.map(data[['latitude', 'longitude']])
else:
    st.write("No 'lat' and 'lon' columns in the data")