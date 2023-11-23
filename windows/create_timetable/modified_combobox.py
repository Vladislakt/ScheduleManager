from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox


class ModifiedQComboBox(QComboBox):
    def __init__(self, row, column, scrollWidget=None, *args, **kwargs):
        super(ModifiedQComboBox, self).__init__(*args, **kwargs)
        self.row = row
        self.column = column
        self.scrollWidget = scrollWidget
        self.setFocusPolicy(Qt.StrongFocus)

    def get_row(self):
        return self.row

    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus():
            return QComboBox.wheelEvent(self, *args, **kwargs)
        else:
            return self.scrollWidget.wheelEvent(*args, **kwargs)
