CREATE TABLE IF NOT EXISTS states (
    state_id SERIAL,
    name varchar(255) not null unique,
    PRIMARY KEY(state_id)
);

CREATE TABLE IF NOT EXISTS cities (
    city_id SERIAL,
    name varchar(255) not null unique,
    state int not null,
    PRIMARY KEY (city_id),
    FOREIGN KEY (state) REFERENCES states (state_id)
);

CREATE TABLE IF NOT EXISTS address_types (
    address_type_id SERIAL,
    name varchar(255) not null unique,
    PRIMARY KEY (address_type_id)
);

CREATE TABLE IF NOT EXISTS service_calls (
    call_id SERIAL,
    crime_id int not null,
    original_crime_type_name varchar(255) not null,
    report_date date not null,
    offense_date date not null,
    call_date_time date not null,
    disposition varchar(255) null,
    address varchar(255) not null,
    city int null,
    address_type INTEGER NOT NULL,
    common_location VARCHAR(255) NOT NULL,
    PRIMARY KEY (call_id),
    FOREIGN KEY (city) REFERENCES cities(city_id),
    FOREIGN KEY (address_type) REFERENCES address_types (address_type_id)
);
