from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import QtCore, QtWidgets
from MainWindow import Ui_MainWindow


class MainWindowExt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.total_customers = 0
        self.total_students = 0
        self.total_revenue = 0


        self.ui.pushButtonCalculate.clicked.connect(self.calculate_payment)
        self.ui.pushButtonNewSelling.clicked.connect(self.new_selling)
        self.ui.pushButtonStaistic.clicked.connect(self.show_statistics)
        self.ui.pushButtonExit.clicked.connect(self.exit_app)

    def calculate_payment(self):
        """Tính toán tổng tiền phải trả"""
        customer_name = self.ui.lineEditCustomerName.text().strip()
        quantity_text = self.ui.lineEditQuantity.text().strip()
        if not customer_name:
            QMessageBox.warning(self, "Input Error", "Customer name cannot be empty.")
            return

        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))
            return

        # Giá sách mỗi cuốn là 20000
        unit_price = 20000
        total_payment = quantity * unit_price

        # Nếu khách hàng là sinh viên thì giảm 5% giá trị
        if self.ui.checkStudent.isChecked():
            total_payment *= 0.95
            self.total_students += 1  # Cập nhật số lượng sinh viên

        # Cập nhật thông tin thống kê
        self.total_customers += 1
        self.total_revenue += total_payment

        # Hiển thị kết quả
        self.ui.lineEditPayment.setText(f"{total_payment:,.0f}")

    def new_selling(self):
        """Làm mới thông tin bán hàng"""
        self.ui.lineEditCustomerName.clear()
        self.ui.lineEditQuantity.clear()
        self.ui.lineEditPayment.clear()
        self.ui.checkStudent.setChecked(False)
        self.ui.lineEditCustomerName.setFocus()

    def show_statistics(self):
        """Hiển thị thông tin thống kê"""
        self.ui.lineEditTotalnumberofCustomers.setText(str(self.total_customers))
        self.ui.lineEditTotalStudentscuston.setText(str(self.total_students))
        self.ui.lineEditTotalRevenue.setText(f"{self.total_revenue:,.0f}")

    def exit_app(self):
        """Thoát ứng dụng"""
        self.close()

