from typing import List, Union

import pygsheets


class GoogleTable:
    """
    Класс для работы с Google Sheet.
    """

    def __init__(
        self, credence_service_file: str = "", googlesheet_file_url: str = ""
    ) -> None:
        """
        Инициализирует класс.
        Args:
            credence_service_file (str): Путь до сервисного файла .json (Google Sheet API).
            googlesheet_file_url (str): Ссылка на Google Sheet.
        Returns: None
        """
        self.credence_service_file = credence_service_file
        self.googlesheet_file_url = googlesheet_file_url

    def _get_googlesheet_by_url(
        self, googlesheet_client: pygsheets.client.Client
    ) -> pygsheets.Spreadsheet:
        """Получает Google. Docs таблицу по ссылке на документ."""
        sheets: pygsheets.Spreadsheet = googlesheet_client.open_by_url(
            self.googlesheet_file_url
        )
        return sheets.sheet1

    def _get_googlesheet_client(self):
        """
        Авторизуется с помощью сервисного ключа и
        возвращает клиентский объект Google Docs.
        """
        return pygsheets.authorize(service_file=self.credence_service_file)

    def search_abonement(
        self,
        data: List[List[Union[str, bool]]],
        search_col: int = 1,
        name_in_table: str = 2,
        balance_col: int = 4,
        end_date_col: int = 5,
    ) -> Union[List[str], int]:
        """
        Возвращает информацию из определенных столбцов таблицы (куда записаны абонементы).
        Args:
            data (List[List[Union[str, bool]]]): Данные для поиска в таблице.
            search_col (int): Диапазон поиска по столбцам.
            name_in_table (str): Имя пользователя в таблице
            balance_col (int): Нормер столбца таблицы с Балансом
            end_date_col (int): Нормер столбца таблицы с Датой окончания действия абонимента
        Returns (List[str]|int):
            Возвращает список с Датой окончания действия абонимента и Балансом
            или -1 если абонемент не найден.
        """
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)
        try:
            find_cell = wks.find(
                data, matchEntireCell=True, cols=(search_col, search_col)
            )[0]
        except:
            return -1
        find_cell_row = find_cell.row
        user_name_in_sheet = wks.get_value((find_cell_row, name_in_table))
        end_date = wks.get_value((find_cell_row, end_date_col))
        balance = wks.get_value((find_cell_row, balance_col))
        return [end_date, balance, user_name_in_sheet]
