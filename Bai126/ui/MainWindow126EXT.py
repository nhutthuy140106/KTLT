from K24406H.Chuong6_ThuVien.Bai126.ui.MainWindow126 import Ui_MainWindow
import sys
import pandas as pd
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QInputDialog

class MainWindow126EXT(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv('../Data/TCB_2018_2020.csv')  # Đọc dữ liệu từ file CSV
        print(self.df)
        self.setupUi(self.MainWindow)  # Cài đặt giao diện từ Ui_MainWindow
        self.setupSignalAndSlot()  # Cài đặt sự kiện cho các nút
        self.display_data(self.df)  # Hiển thị dữ liệu ban đầu

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        # Kết nối các nút với các phương thức xử lý
        self.pushButton.clicked.connect(self.search_day)  # Nút tìm kiếm theo ngày
        self.pushButton_2.clicked.connect(self.search_multiple_days)  # Nút tìm kiếm nhiều ngày
        self.pushButton_3.clicked.connect(self.filter_price)  # Nút lọc theo giá trị
        self.pushButton_4.clicked.connect(self.display_data)  # Nút hiển thị lại dữ liệu

    def search_day(self):
        """Tìm kiếm dữ liệu theo một ngày (chỉ nhập ngày dd)"""
        day_input = self.dayInputField.text()  # Lấy giá trị ngày nhập từ người dùng

        # Lọc dữ liệu theo ngày (kiểm tra phần ngày trong cột 'Date')
        filtered_day = self.df[self.df['Date'].str.endswith(day_input)]  # Kiểm tra ngày

        # Hiển thị dữ liệu lên bảng
        self.display_data(filtered_day)

    def search_multiple_days(self):
        """Tìm kiếm dữ liệu theo mảng ngày"""
        days_input = self.dayInputField.text().split(',')  # Nhập và tách các ngày bằng dấu phẩy

        # Lọc dữ liệu theo mảng các ngày
        filtered_days = self.df[self.df['Date'].str.endswith(tuple(days_input))]  # Kiểm tra ngày trong cột 'Date'

        # Hiển thị dữ liệu lên bảng
        self.display_data(filtered_days)

    def filter_price(self):
        """Lọc dữ liệu theo giá trị x và y từ bàn phím"""
        x, ok1 = QInputDialog.getDouble(self, "Nhập x", "Nhập giá trị x (giới hạn dưới của Price):")
        if not ok1:  # Nếu không nhập giá trị x, thoát
            return

        y, ok2 = QInputDialog.getDouble(self, "Nhập y", "Nhập giá trị y (giới hạn trên của Price):")
        if not ok2:  # Nếu không nhập giá trị y, thoát
            return

        # Lọc dữ liệu theo điều kiện x < Close < y
        filtered_df = self.df[(self.df['Close'] > x) & (self.df['Close'] < y)]

        # Hiển thị kết quả lọc
        self.display_data(filtered_df)

    def display_data(self, filtered_df=None):
        """Hiển thị dữ liệu lên bảng"""
        if filtered_df is None:
            filtered_df = self.df  # Nếu không có dữ liệu lọc, hiển thị tất cả dữ liệu

        rows, cols = filtered_df.shape
        self.tableWidget.setRowCount(rows)  # Cập nhật số lượng dòng
        self.tableWidget.setColumnCount(cols)  # Cập nhật số lượng cột

        # Thiết lập tiêu đề cột
        self.tableWidget.setHorizontalHeaderLabels(filtered_df.columns)

        # Thêm dữ liệu vào bảng
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(str(filtered_df.iloc[row, col]))
                self.tableWidget.setItem(row, col, item)
