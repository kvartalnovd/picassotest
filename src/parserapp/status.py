from datetime import datetime, timedelta
from pathlib import Path
from random import choice
from typing import Optional

from config import APP_NAME

import logging


def get_logger(log_file: Path) -> logging.Logger:
    log = logging.getLogger(APP_NAME)
    log.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
    file_handler.setFormatter(basic_formater)
    log.addHandler(file_handler)
    return log


class ProgressBar:
    LOADING_ELEMENT = '█'
    LOADING_ELEMENT_NUMBER = 50
    SPEED_CHECK_FREQUENCY_SECONDS = 1
    CHANGE_FREQUENCY_PER_PERCENT = 1.0
    LOADER_SYMBOLS = tuple('😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 😉 😊 😇 🥰 😍 🤩 😘 😗 😚 😙 😋 😛 😜 🤪 😝 🤑 🤗 🤭 🤫 🤔 🤐 '
                           '🤨 😐 😑 😶 😏 😒 🙄 😬 🤥 😌 😔 😪 🤤 😴 😷 🤒 🤕 🤢 🤮 🤧 🥵 🥶 🥴 😵 🤯 🤠 🥳 😎 🤓 🧐 😕 '
                           '😟 🙁 😮 😯 😲 😳 🥺 😦 😧 😨 😰 😥 😢 😭 😱 😖 😣 😞 😓 😩 😫 😤 😡 😠 🤬 😈 👿 💀 💩 🤡 👹 '
                           '👺 👻 👽 👾 🤖 😺 😸 😹 😻 😼 😽 🙀 😿 😾 🙈 🙉 🙊'.split())

    def __init__(self, total_elements_number: int, start_time: datetime, frequency_value: str = 'rows/sec') -> None:
        self.__total_elements_number: int = total_elements_number
        self.__frequency_value: str = frequency_value
        self.__start_time: datetime = start_time
        self.__last_speed_calculation: datetime = datetime.now()
        self.__upload_speed: float = .0  # elements loading per second
        self.__loader_icon = choice(ProgressBar.LOADER_SYMBOLS)

    def update(self, completed_elements: int = 0) -> None:
        speed_update_delta: timedelta = datetime.now() - self.__last_speed_calculation
        if speed_update_delta.seconds >= ProgressBar.SPEED_CHECK_FREQUENCY_SECONDS:
            start_time_delta = datetime.now() - self.__start_time
            self.__upload_speed = float('{:.3f}'.format(completed_elements / start_time_delta.seconds))
            self.__last_speed_calculation = datetime.now()
        self.__render(completed_elements)

    def __render(self, completed_elements: int) -> None:
        loading_percentage = float('{:.3f}'.format(completed_elements / self.__total_elements_number * 100))
        completed_progress_bar_parts = int((ProgressBar.LOADING_ELEMENT_NUMBER * loading_percentage) / 100)
        uncompleted_progress_bar_parts = ProgressBar.LOADING_ELEMENT_NUMBER - completed_progress_bar_parts
        progress_bar_line = f'{ProgressBar.LOADING_ELEMENT * completed_progress_bar_parts}' \
                            f'{" " * (uncompleted_progress_bar_parts + 1)}'
        percent_status = f'{loading_percentage}%{" " * (6 - len(str(loading_percentage)))}'
        upload_speed_status = f'{"" * (10 - len(str(self.__upload_speed)))}{self.__upload_speed} ' \
                              f'{self.__frequency_value} ' \
                              f'({completed_elements} / {self.__total_elements_number})'
        if loading_percentage % ProgressBar.CHANGE_FREQUENCY_PER_PERCENT == .0:
            self.__change_loader_icon()
        result_delta = datetime.now() - self.__start_time
        time_status_value = str(timedelta(seconds=result_delta.seconds))
        print(f'\r [{time_status_value}] {self.__loader_icon} '
              f'| {progress_bar_line} '
              f'| {percent_status} '
              f'| ~ {upload_speed_status}',
              end='')

    @staticmethod
    def init_label(label: str) -> None:
        print(f'\n [Loading]    > {label}{" " * (ProgressBar.LOADING_ELEMENT_NUMBER - len(label))} <')

    def __change_loader_icon(self) -> None:
        self.__loader_icon = choice(ProgressBar.LOADER_SYMBOLS)


class StatusManager:

    def __init__(self, total_elements_number: int, label: str, start_timer_immediately: bool = True) -> None:
        self.__label = label
        self.__total_elements_number: int = total_elements_number
        self.__completed_elements: int = 0

        self.__start_time: Optional[datetime] = datetime.now() if start_timer_immediately else None
        self.__progressbar = ProgressBar(
            total_elements_number=self.__total_elements_number,
            start_time=self.__start_time
        )

        if start_timer_immediately:
            self.__progressbar.init_label(self.__label)

    def update(self) -> None:
        if not isinstance(self.__start_time, datetime):
            self.__start_time = datetime.now()
            self.__progressbar.init_label(self.__label)
        self.__completed_elements += 1
        self.__progressbar.update(self.__completed_elements)

    def reset_timer(self) -> None:
        self.__start_time = datetime.now()

    def get_result_status(self) -> str:
        result_delta = datetime.now() - self.__start_time
        total_time_value = str(timedelta(seconds=result_delta.seconds))
        return f'{self.__completed_elements} elements processed in {total_time_value}'


class StatusService:

    def __init__(self, log_file: Path) -> None:
        self.__logger = get_logger(log_file)

    def log(self, message: str) -> None:
        dt = datetime.now()
        app_message = f' {APP_NAME} [{dt.strftime("%d.%m.%Y %H:%M:%S")}] > {message}'
        print(app_message)
        self.__logger.info(message)

    @staticmethod
    def get_status_manager(total_elements_number: int, label: str) -> StatusManager:
        return StatusManager(total_elements_number, label)
