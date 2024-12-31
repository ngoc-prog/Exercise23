import sys
from PyQt6.QtWidgets import QApplication
from MainWindowExt import MainWindowExt

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Khởi tạo cửa sổ chính
    main_window = MainWindowExt()
    main_window.show()

    # Chạy ứng dụng
    sys.exit(app.exec())
