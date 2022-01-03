drop database if exists EventManagementSystem;
create database EventManagementSystem;
use EventManagementSystem;

create table events (
    id varchar(10) primary key not null,
    name tinytext not null,
    description text not null,
    event_manager tinytext not null,
    start_date date not null,
    end_date date not null,
    budget int not null,
    location tinytext not null
);
