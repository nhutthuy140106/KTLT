import pandas as pd

df = pd.read_csv('TCB_2018_2020.csv')
print(df)

x = float(input("Nhập giá trị x (giới hạn dưới của Close): "))
y = float(input("Nhập giá trị y (giới hạn trên của Close): "))
filtered_df = df[(df['Close'] > x) & (df['Close'] < y)]
print(filtered_df)

df_filtered_columns = df[['Date', 'High', 'Low', 'Close']]
print(df_filtered_columns)

day_input = input("Nhập ngày cần tìm dd: ")
filtered_day = df[df['Date'].str.endswith(day_input)]
if not filtered_day.empty:
    print(filtered_day)
else:
    print(f"Không có dữ liệu cho ngày {date_input}")

days_input = input("Nhập các ngày cần lọc (cách nhau bởi dấu phẩy, theo định dạng dd): ").split(',')
filtered_days = df[df['Date'].str.endswith(tuple(days_input))]
if not filtered_days.empty:
    print(filtered_days)
else:
    print(f"Không có dữ liệu cho các ngày {', '.join(days_input)}")