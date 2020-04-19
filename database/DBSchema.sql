CREATE SCHEMA umschedulerschema;

USE umschedulerschema;

CREATE TABLE Users(
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
    type VARCHAR(30) NOT NULL,
    first VARCHAR(30) NOT NULL, 
    last VARCHAR(30) NOT NULL,
    address VARCHAR(256) NOT NULL,
    zip INT,
    phone varchar(10),
    email VARCHAR(256),
    password varchar(256),
    PRIMARY KEY (id)
);