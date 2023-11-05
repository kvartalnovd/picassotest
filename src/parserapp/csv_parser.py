from pathlib import Path

import pandas as pd


class CsvParser:

    def __init__(self, csv_file: Path) -> None:
        self.__df = CsvParser.load_normalized_dataframe(csv_file)

    @property
    def df(self):
        return self.__df

    def row_count(self) -> int:
        row_num, _ = self.__df.shape
        return row_num

    def is_columns_eq_to(self, columns: list) -> bool:
        return list(self.__df.columns).sort() == columns.sort()

    @staticmethod
    def load_normalized_dataframe(csv_file: Path):
        df = pd.read_csv(csv_file, nrows=10000)

        # Normalize df's column names
        old_column_names = list(df.columns)
        new_column_names = list(map(lambda x: x.lower().replace(' ', '_'), df.columns))
        df.rename(columns=dict(zip(old_column_names, new_column_names)), inplace=True)
        return df
