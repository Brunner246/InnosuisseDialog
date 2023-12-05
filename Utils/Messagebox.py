from PyQt5.QtWidgets import QMessageBox


def show_info_box(parent, seconds: float):
    QMessageBox.information(parent, "Info", f"Elapsed time for creating the text objects: {seconds} seconds")