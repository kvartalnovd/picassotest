from datetime import datetime
from typing import Optional

from psycopg2.errors import UniqueViolation

import config
from csv_parser import CsvParser
from database import PostgreSQL
from database.models import State, City, AddressTypes, ServiceCall
from status import StatusService


class ServiceCallParser:
    LOG_FILE = config.LOG_DIR.joinpath('service_call_parser.log')
    SERVICE_CALL_COLUMNS = [
        'OriginalCrimeTypeName', 'ReportDate', 'CallDate', 'OffenseDate', 'CallTime', 'CallDateTime', 'Disposition',
        'Address', 'City', 'State', 'AgencyId', 'AddressType', 'CommonLocation'
    ]

    def __init__(self) -> None:
        self.__status_service = StatusService(
            log_file=ServiceCallParser.LOG_FILE,
        )

        self.__database = PostgreSQL(
            container_name=config.PG_CONTAINER_NAME,
            dbname=config.PG_DBNAME,
            username=config.PG_USERNAME,
            password=config.PG_PASSWORD)
        self.__csv_parser = CsvParser(csv_file=config.INIT_SERVICE_CALL_DATA)

    def run(self) -> None:
        self.__upload_service_call()
        self.__database.close()

    def __upload_service_call(self) -> None:
        self.__status_service.log(f'Start uploading {self.__csv_parser.row_count()} rows into the database')
        service_call_status_manager = self.__status_service.get_status_manager(
            total_elements_number=self.__csv_parser.row_count(),
            label='Service Calls Uploading to Database'
        )

        for _, row in self.__csv_parser.df.iterrows():
            report_date = datetime.strptime(row["report_date"], '%Y-%m-%dT%H:%M:%S')
            offense_date = datetime.strptime(row["offense_date"], '%Y-%m-%dT%H:%M:%S')
            call_date_time = datetime.strptime(row["call_date_time"], '%Y-%m-%dT%H:%M:%S')

            state: State = self.__database.get_or_create(model=State, name=row["state"]).state_id

            city_name = row["city"]
            city: Optional[City] = self.__database.get_or_create(model=City, name=city_name,
                                                                 state=state).city_id \
                if isinstance(city_name, str) and city_name.lower() == 'nan' \
                else None
            address_type: AddressTypes = self.__database.get_or_create(model=AddressTypes,
                                                                       name=row['address_type']).address_type_id

            common_location_value = row['common_location']
            common_location = common_location_value \
                if isinstance(common_location_value, str) and common_location_value.lower() != 'nan' \
                else 'Not recorded'

            try:
                self.__database.create_if_not_exists(
                    model=ServiceCall,
                    verification_field='crime_id',

                    crime_id=row['crime_id'],
                    original_crime_type_name=row['original_crime_type_name'],
                    report_date=report_date,
                    offense_date=offense_date,
                    call_date_time=call_date_time,
                    disposition=row['disposition'],
                    address=row['address'],
                    city=city,
                    address_type=address_type,
                    common_location=common_location
                )
            except UniqueViolation:
                service_call_status_manager.error_report('UniqueViolation')
            except KeyboardInterrupt:
                break

            service_call_status_manager.update()

        result_status = service_call_status_manager.get_result_status(result_title='Upload completed successfully',
                                                                      element_label='row')
        print('\n')
        self.__status_service.log(result_status)
        print('\n')

    def __check_df(self) -> None:
        if not self.__csv_parser.is_columns_eq_to(ServiceCallParser.SERVICE_CALL_COLUMNS):
            self.__status_service.log('The uploaded file contains incorrect columns')
            raise ValueError


if __name__ == '__main__':
    app = ServiceCallParser()
    app.run()
