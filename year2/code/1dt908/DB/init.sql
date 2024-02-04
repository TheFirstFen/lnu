-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hotell_temp
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema hotel_temp
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotel_temp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel_temp` DEFAULT CHARACTER SET utf8mb3 ;
USE `hotel_temp` ;

-- -----------------------------------------------------
-- Table `hotel_temp`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_temp`.`customer` (
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
-- Table `hotel_temp`.`worker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_temp`.`worker` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(100) NOT NULL,
  `loginName` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `tel` VARCHAR(100) NOT NULL,
  `role` VARCHAR(100) NOT NULL,
  `hotel` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`userid`, `loginName`),
  UNIQUE INDEX `userid_UNIQUE` (`userid` ASC) VISIBLE,
  UNIQUE INDEX `loginName_UNIQUE` (`loginName` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `hotel_temp`.`room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_temp`.`room` (
  `roomid` INT NOT NULL AUTO_INCREMENT,
  `roomnr` INT NOT NULL,
  `roomsize` INT NOT NULL,
  `roomtype` VARCHAR(100) NOT NULL,
  `price` FLOAT NOT NULL,
  `hotel` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`roomid`),
  UNIQUE INDEX `roomid_UNIQUE` (`roomid` ASC) VISIBLE,
  UNIQUE INDEX `roomnr_UNIQUE` (`roomnr` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel_temp`.`booking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel_temp`.`booking` (
  `bookingid` INT NOT NULL AUTO_INCREMENT,
  `startdate` DATE NOT NULL,
  `enddate` DATE NOT NULL,
  `roomid` VARCHAR(100) NOT NULL,
  `customerid` INT NOT NULL,
  `paid` INT NOT NULL,
  `totalprice` FLOAT NOT NULL,
  `guestamount` INT NOT NULL,
  `createdby` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`bookingid`),
  UNIQUE INDEX `bookingid_UNIQUE` (`bookingid` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Create an admin user with privileges only for the 'hotel_temp' database
-- -----------------------------------------------------
CREATE USER 'hotel2_admin'@'%' IDENTIFIED BY 'admin';

GRANT USAGE ON *.* TO 'hotel2_admin'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON hotel_temp.* TO 'hotel2_admin'@'%';
-- GRANT ALL PRIVILEGES ON hotel_temp.* TO 'hotel2_admin'@'%';
FLUSH PRIVILEGES;
