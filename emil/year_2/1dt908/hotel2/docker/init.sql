-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hotel2_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotel2_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel2_db` DEFAULT CHARACTER SET utf8mb3 ;
USE `hotel2_db` ;

-- -----------------------------------------------------
-- Table `hotel2_db`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel2_db`.`customer` (
  `customerid` INT NOT NULL AUTO_INCREMENT,
  `fName` VARCHAR(100) NOT NULL,
  `lName` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `tel` VARCHAR(100) NOT NULL,
  `paymentmethod` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`customerid`),
  UNIQUE INDEX `customerid_UNIQUE` (`customerid` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `tel_UNIQUE` (`tel` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hotel2_db`.`worker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel2_db`.`worker` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(100) NOT NULL,
  `loginName` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `tel` VARCHAR(100) NOT NULL,
  `role` VARCHAR(100) NOT NULL,
  `hotel` VARCHAR(100) NOT NULL,
  `status` INT NOT NULL,
  PRIMARY KEY (`userid`, `loginName`),
  UNIQUE INDEX `userid_UNIQUE` (`userid` ASC) VISIBLE,
  UNIQUE INDEX `loginName_UNIQUE` (`loginName` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hotel2_db`.`room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel2_db`.`room` (
  `roomid` INT NOT NULL AUTO_INCREMENT,
  `roomnr` INT NOT NULL,
  `roomsize` INT NOT NULL,
  `roomtype` VARCHAR(100) NOT NULL,
  `price` FLOAT NOT NULL,
  `hotel` VARCHAR(100) NOT NULL,
  `status` INT NOT NULL,
  PRIMARY KEY (`roomid`),
  UNIQUE INDEX `roomid_UNIQUE` (`roomid` ASC) VISIBLE,
  UNIQUE INDEX `roomnr_UNIQUE` (`roomnr` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel2_db`.`booking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel2_db`.`booking` (
  `bookingid` INT NOT NULL AUTO_INCREMENT,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `customerid` INT NOT NULL,
  `paid` INT NOT NULL,
  `totalprice` FLOAT NOT NULL,
  `guestamount` INT NOT NULL,
  `createdby` VARCHAR(100) NOT NULL,
  `checkout` INT NOT NULL,
  `checkin` VARCHAR(45) NOT NULL,
  `status` INT NOT NULL,
  PRIMARY KEY (`bookingid`),
  UNIQUE INDEX `bookingid_UNIQUE` (`bookingid` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF Not Exists `hotel2_db`.`booking_room` (
    bookingid INT,
    roomid INT,
    FOREIGN KEY (bookingid) REFERENCES booking(bookingid),
    FOREIGN KEY (roomid) REFERENCES room(roomid)
);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Create an admin user with privileges only for the 'hotel2_db' database
-- -----------------------------------------------------
CREATE USER 'hotel2_admin'@'%' IDENTIFIED BY 'admin';

GRANT USAGE ON hotel2_db.* TO 'hotel2_admin'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON hotel2_db.* TO 'hotel2_admin'@'%';
GRANT ALL PRIVILEGES ON hotel2_db.* TO 'hotel2_admin'@'%';
FLUSH PRIVILEGES;

-- -----------------------------------------------------
-- Adding testsing data to database
-- -----------------------------------------------------
-- Workers (INSERT -- Password)
-- Standard Accounts
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("c1c224b03cd9bc7b6a86d77f5dace40191766c485cd55dc48caf9ac873335d6f", "admin", "admin@hotel2.com", "0100000000", "1", "hotel2", 0); -- Admin
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("ce5ca673d13b36118d54a7cf13aeb0ca012383bf771e713421b4d1fd841f539a", "reception", "reception@hotel2.com", "0200000000", "0", "hotel2", 0); -- toor

-- User Accounts
-- Admistrator
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("d3bb08b2a5413ec0d8295ce574dff2220e7b6c3d15bbd18fd8452b0d30245450", "tobias", "tobias@hotel2.com", "0100000001", "1", "hotel2", 0); -- tobias@hotel2
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("bdb03a594c6d5bac70011a122640e33ce0e48eea028f38f8791b01665560186c", "imad", "imad@hotel2.com", "0100000002", "1", "hotel2", 0); -- imad@hotel2
-- Receptionist
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("1b858284d003d47e775eee1e285a09bade6fe12b5aa99e2e3ac88b28ac7ef0fc", "jesper", "jesper@hotel2.com", "0200000001", "0", "hotel2", 0); -- jesper@hotel2
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("71f2222b38ae4de44a9ae4853a03257545c0bc3b048965288bf27f61cf3bfede", "emil", "emil@hotel2.com", "0200000002", "0", "hotel2", 0); -- emil@hotel2
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("6acb06f23a8a0d8ca29f5ff6198c2d47ba2ca55dce6e0895d443bc5ca0492305", "samuel", "samuel@hotel2.com", "0200000003", "0", "hotel2", 0); -- samuel@hotel2
INSERT INTO worker (password, loginName, email, tel, role, hotel, status) VALUES ("70a872fa6cbf20dadefb093efaafb1b8aac3e69485def25a3b73827aa44da729", "tobias1", "tobias1@hotel2.com", "0200000004", "0", "hotel2", 0); -- tobias1@hotel2

-- Customers
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Tobias", "Ohlsson", "0800000000", "tobias.ohlsson@lnu.se", "Swish");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Emil", "Ulvagården", "0900000000", "eu222dq@student.lnu.se", "PayPal");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Samuel", "Berg", "0600000000", "sb224sc@student.lnu.se", "Kort");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Jesper", "Wingren", "0500000000", "jw223rn@student.lnu.se", "Kort");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Imad", "Tabikh", "0400000000", "it222gs@student.lnu.se", "PayPal");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Agust", "Eliasson", "0300000000", "ae224pp@student.lnu.se", "Swish");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Kim", "Wong", "0800000001", "kw222qs@student.lnu.se", "Swish");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Petter", "Gustafsson", "0900000001", "pg222jw@student.lnu.se", "PayPal");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Elliot", "Ehn", "0600000001", "ee223zs@student.lnu.se", "Kort");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Emil", "Ringdahl", "0500000001", "er223gj@student.lnu.se", "Kort");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Max", "Hoffman", "0400000001", "ma226pv@student.lnu.se", "PayPal");
INSERT INTO customer (fName, lName, tel, email, paymentmethod) VALUES ("Mehrtash", "Darvish", "0300000001", "md223iy@student.lnu.se", "Swish");

-- Rooms
-- Våning 1
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("101", "4", "Standard", "100.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("102", "2", "Deluxe", "125.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("103", "1", "Standard", "25.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("104", "3", "Deluxe", "175.0", "hotel2", 0);
-- Våning 2
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("201", "4", "Standard", "115.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("202", "2", "Deluxe", "112.5", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("203", "1", "Standard", "35.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("204", "3", "Deluxe", "180.0", "hotel2", 0);
-- Våning 3
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("301", "4", "Standard", "75.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("302", "2", "Deluxe", "130.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("303", "1", "Standard", "30.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("304", "3", "Deluxe", "150.0", "hotel2", 0);
-- Våning 4
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("401", "4", "Standard", "125.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("402", "2", "Deluxe", "150.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("403", "1", "Standard", "50.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("404", "3", "Deluxe", "225.0", "hotel2", 0);
-- Våning 5
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("501", "4", "Standard", "125.0", "hotel2", 1);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("502", "2", "Deluxe", "150.0", "hotel2", 1);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("503", "1", "Standard", "50.0", "hotel2", 1);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("504", "3", "Deluxe", "225.0", "hotel2", 1);
-- Våning 6
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("601", "4", "Standard", "125.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("602", "2", "Deluxe", "150.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("603", "1", "Standard", "50.0", "hotel2", 0);
INSERT INTO room (roomnr, roomsize, roomtype, price, hotel, status) VALUES ("704", "3", "Deluxe", "225.0", "hotel2", 0);

-- Bookings
-- Check-in
INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-03-19", "%Y-%m-%d"), STR_TO_DATE("2024-03-21", "%Y-%m-%d"), "3", "0", "100.0", "4", "9", "0", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (1, "1");

INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-03-19", "%Y-%m-%d"), STR_TO_DATE("2024-03-26", "%Y-%m-%d"), "5", "0", "125.0", "2", "5", "0", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (2, "2");

INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-03-19", "%Y-%m-%d"), STR_TO_DATE("2024-04-02", "%Y-%m-%d"), "7", "0", "175.0", "3", "6", "0", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (3, "4");

INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-03-19", "%Y-%m-%d"), STR_TO_DATE("2024-03-24", "%Y-%m-%d"), "9", "0", "35.0", "1", "8", "0", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (4, "7");

-- Check-out
INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-02-14", "%Y-%m-%d"), STR_TO_DATE("2024-03-19", "%Y-%m-%d"), "14", "0", "300.0", "5", "7", "1", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (5, "2");
INSERT INTO booking_room (bookingid, roomid) VALUES (5, "4");

INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-02-03", "%Y-%m-%d"), STR_TO_DATE("2024-03-19", "%Y-%m-%d"), "6", "1", "130.0", "2", "9", "1", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (6, "10");

INSERT INTO booking (startdate, enddate, customerid, paid, totalprice, guestamount, createdby, checkin, checkout, status) VALUES (STR_TO_DATE("2024-02-12", "%Y-%m-%d"), STR_TO_DATE("2024-03-19", "%Y-%m-%d"), "11", "1", "125.0", "4", "7", "1", "0", 0);
INSERT INTO booking_room (bookingid, roomid) VALUES (7, "13");