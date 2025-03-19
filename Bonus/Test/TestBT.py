import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Đọc dữ liệu từ file Excel
df = pd.read_excel('../Dataset/dataset-406H.xlsx')
print(df.head())  # Kiểm tra dữ liệu

# Phân tích dữ liệu từ dataset Gapminder cho năm 2007 và châu Âu
df_gapminder = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")

# Cập nhật các quốc gia có dân số nhỏ hơn 2.6 triệu thành 'Other countries'
df_gapminder.loc[df_gapminder['pop'] < 2.6e6, 'country'] = 'Other countries'

# Vẽ biểu đồ Pie với Plotly
fig = px.pie(df_gapminder, values='pop', names='country', title='Population of European continent')
fig.show()

# Dữ liệu cho biểu đồ Sunburst (cấu trúc tổ chức)
character = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parent = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Seth", "Eve", "Awan", "Eve"]
value = [10, 14, 12, 12, 10, 2, 6, 6, 4, 4]

# Kiểm tra độ dài các mảng
print(len(character), len(parent), len(value))  # Kiểm tra độ dài các mảng

# Kiểm tra nếu độ dài không giống nhau, sửa lại
max_length = max(len(character), len(parent), len(value))

# Nếu một trong các mảng có chiều dài nhỏ hơn max_length, bổ sung NaN vào
if len(character) < max_length:
    character.extend([None] * (max_length - len(character)))

if len(parent) < max_length:
    parent.extend([None] * (max_length - len(parent)))

if len(value) < max_length:
    value.extend([None] * (max_length - len(value)))

# Kiểm tra lại độ dài các mảng
print(len(character), len(parent), len(value))

# Chuyển dict thành DataFrame
data = dict(character=character, parent=parent, value=value)
df_sunburst = pd.DataFrame(data)

# Vẽ biểu đồ Sunburst
fig_sunburst = px.sunburst(
    df_sunburst,  # Truyền DataFrame thay vì dict
    names='character',
    parents='parent',
    values='value',
    title="Family Tree Sunburst Chart"
)

fig_sunburst.show()
