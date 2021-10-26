drop database if exists EventManagementSystem;
create database EventManagementSystem;
use EventManagementSystem;

create table events (
    id varchar(10) primary key not null,
    name tinytext not null,
    description text not null,
    `date` date not null
);

create table recycle_bin (
    id varchar(10) primary key not null,
    name tinytext not null,
    description text not null,
    `date` date not null
);
