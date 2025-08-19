


-- create table if not exists parent(
--     id bigserial primary key,
--     name varchar(100) not null,
--     email varchar(250) not null UNIQUE
    
-- );

DROP TABLE IF EXISTS parent_address;
create table if not exists parent_address(
    id bigserial primary key,
    parent_id BIGSERIAL REFERENCES parent(id),
    county_name varchar (250),
    town varchar (250),
    longitutde real,
    latitude real,
    house_no varchar(200)

);

-- DROP TABLE IF EXISTS parent_address;
-- create table if not exists parent_address(
--     id bigserial primary key,
--     parent_email varchar(250) REFERENCES parent(email),
--     county_name varchar (250),
--     town varchar (250)
-- );



-- insert into parent
-- (name, email)
-- values
-- ('john doey', 'john@gmail.com'),
-- ('jane doey', 'jane@gmail.com'),
-- ('greg miles', 'greg@gmail.com'),
-- ('checksy miles', 'checksy@gmail.com');

insert into parent_address
(county_name, town, longitutde, latitude, house_no)
values
('Nairobi', 'langata', 0, 7, '123'),
('Nairobi', 'gigiri', 034, 0, '1723')


