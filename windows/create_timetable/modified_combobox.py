from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox


class ModifiedQComboBox(QComboBox):
    def __init__(self, row, column, scroll_widget=None, *args, **kwargs):
        super(ModifiedQComboBox, self).__init__(*args, **kwargs)
        self.row = row
        self.column = column
        self.scrollWidget = scroll_widget
        self.setFocusPolicy(Qt.StrongFocus)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus():
            return QComboBox.wheelEvent(self, *args, **kwargs)
        else:
            return self.scrollWidget.wheelEvent(*args, **kwargs)
