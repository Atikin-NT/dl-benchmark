from tags import CONFIG_IP_TAG, CONFIG_LOGIN_TAG, CONFIG_PASSWORD_TAG, CONFIG_OS_TAG, CONFIG_DOWNLOAD_FOLDER_TAG

from .table import Table


class DeployConfigTable(Table):
    def __init__(self, parent):
        super().__init__(parent)
        self.__headers = [CONFIG_IP_TAG, CONFIG_LOGIN_TAG, CONFIG_PASSWORD_TAG, CONFIG_OS_TAG,
                          CONFIG_DOWNLOAD_FOLDER_TAG]
        self._count_col = len(self.__headers)
        self._count_row = 100
        self.setColumnCount(self._count_col)
        self.setRowCount(self._count_row)
        self.setHorizontalHeaderLabels(self.__headers)
        self._resize_columns()
        self.clear()
        self.clicked.connect(self.clicked_table)  # noqa: E1120

    def update(self, computers):
        self.clear()
        count = 0
        for i in range(len(computers)):
            self.setItem(i, 0, self._create_cell(computers[i].ip))
            self.setItem(i, 1, self._create_cell(computers[i].login))
            self.setItem(i, 2, self._create_cell(computers[i].password))
            self.setItem(i, 3, self._create_cell(computers[i].os))
            self.setItem(i, 4, self._create_cell(computers[i].download_folder))
            count += 1
