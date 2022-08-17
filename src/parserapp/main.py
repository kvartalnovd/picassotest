import config
from csv_parser import CsvParser
from database import PsqlDB
from status import StatusService


class ServiceCallParser:
    LOG_FILE = config.LOG_DIR.joinpath('service_call_parser.log')
    SERVICE_CALL_COLUMNS = [
        'OriginalCrimeTypeName', 'ReportDate', 'CallDate', 'OffenseDate', 'CallTime', 'CallDateTime', 'Disposition',
        'Address', 'City', 'State', 'AgencyId', 'AddressType', 'CommonLocation'
    ]

    def __init__(self) -> None:
        self.__database = PsqlDB(
            host_name=config.PG_HOST_NAME,
            dbname=config.PG_DBNAME,
            username=config.PG_USERNAME,
            password=config.PG_PASSWORD,
            port=config.PG_PORT
        )
        self.__csv_parser = CsvParser(csv_file=config.INIT_SERVICE_CALL_DATA)
        self.__status_service = StatusService(
            log_file=ServiceCallParser.LOG_FILE,
        )

    def run(self) -> None:
        print('\n')
        self.__status_service.log(f'Start uploading {self.__csv_parser.row_count()} rows into the database')
        states_handling_status_manager = self.__status_service.get_status_manager(
            total_elements_number=self.__csv_parser.row_count(),
            label='States Uploading to Database'
        )

        row_count = 0
        for index, row in self.__csv_parser.df.iterrows():
            row_count += 1
            states_handling_status_manager.update()

        print('\n')
        self.__status_service.log(f'Upload completed successfully: {row_count} rows of data loaded')
        result_status = states_handling_status_manager.get_result_status()
        self.__status_service.log(result_status)

    def __check_df(self) -> None:
        if not self.__csv_parser.is_columns_eq_to(ServiceCallParser.SERVICE_CALL_COLUMNS):
            self.__status_service.log('The uploaded file contains incorrect columns')
            raise ValueError


if __name__ == '__main__':
    app = ServiceCallParser()
    app.run()
