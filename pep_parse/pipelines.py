import datetime as dt
from pathlib import Path

from .exceptions import NoStatusException

BASE_DIR = Path(__file__).parents[1]
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULTS_DIR = BASE_DIR / 'results'


class PepParsePipeline():
    '''Считает количество PEP по статусам и общее количество'''

    def __init__(self) -> None:
        RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results_data = {}

    def process_item(self, item, spider):
        try:
            status = item['status']
            self.results_data[status] = self.results_data.get(status, 0) + 1
            return item
        except NoStatusException:
            number = item['number']
            print(f'PEP {number} не имеет статуса!')

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        filename = f'{RESULTS_DIR}/status_summary_{now_formatted}.csv'
        total = 0
        with open(
                filename,
                mode='w',
                encoding='utf-8'
        ) as f:
            f.write('Статус, Количество\n')
            for key, value in self.results_data.items():
                total += int(value)
                f.write(f'{key}, {value}\n')
            f.write(f'Total,{total}\n')
