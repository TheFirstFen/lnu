-- MySQL Workbench Forward Engineering
SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS,
    UNIQUE_CHECKS = 0;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS,
    FOREIGN_KEY_CHECKS = 0;
SET @OLD_SQL_MODE = @@SQL_MODE,
    SQL_MODE = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
-- -----------------------------------------------------
-- Schema book_store
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `book_store` DEFAULT CHARACTER SET utf8;
USE `book_store`;
-- -----------------------------------------------------
-- Table `book_store`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`books` (
    `isbn` CHAR(10) NOT NULL,
    `author` VARCHAR(100) NOT NULL,
    `title` VARCHAR(128) NOT NULL,
    `price` FLOAT NOT NULL,
    `subject` VARCHAR(30) NOT NULL,
    PRIMARY KEY (`isbn`)
) ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `book_store`.`members`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`members` (
    `fname` VARCHAR(20) NOT NULL,
    `lname` VARCHAR(20) NOT NULL,
    `address` VARCHAR(50) NOT NULL,
    `city` VARCHAR(30) NOT NULL,
    `state` VARCHAR(20) NOT NULL,
    `zip` INT NOT NULL,
    `phone` VARCHAR(12) NULL,
    `email` VARCHAR(40) NOT NULL,
    `userid` INT NOT NULL AUTO_INCREMENT,
    `password` VARCHAR(80) NULL,
    `creditcardtype` VARCHAR(10) NULL,
    `creditcardnumber` CHAR(16) NULL,
    PRIMARY KEY (`userid`)
) ENGINE = InnoDB;
CREATE UNIQUE INDEX `email_UNIQUE` ON `book_store`.`members` (`email` ASC) VISIBLE;
-- -----------------------------------------------------
-- Table `book_store`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`orders` (
    `userid` INT NOT NULL,
    `ono` INT NOT NULL AUTO_INCREMENT,
    `received` DATE NOT NULL,
    `shipped` DATE NULL,
    `shipAddress` VARCHAR(50) NULL,
    `shipCity` VARCHAR(30) NULL,
    `shipState` VARCHAR(20) NULL,
    `shipZip` INT NULL,
    PRIMARY KEY (`ono`),
    CONSTRAINT `fk_orders_members1` FOREIGN KEY (`userid`) REFERENCES `book_store`.`members` (`userid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;
CREATE INDEX `fk_orders_members1_idx` ON `book_store`.`orders` (`userid` ASC) VISIBLE;
-- -----------------------------------------------------
-- Table `book_store`.`odetails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`odetails` (
    `ono` INT NOT NULL,
    `isbn` CHAR(10) NOT NULL,
    `qty` INT NOT NULL,
    `price` FLOAT NOT NULL,
    PRIMARY KEY (`ono`, `isbn`),
    CONSTRAINT `fk_odetails_books1` FOREIGN KEY (`isbn`) REFERENCES `book_store`.`books` (`isbn`) ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT `fk_odetails_orders1` FOREIGN KEY (`ono`) REFERENCES `book_store`.`orders` (`ono`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;
CREATE INDEX `fk_odetails_books1_idx` ON `book_store`.`odetails` (`isbn` ASC) VISIBLE;
CREATE INDEX `fk_odetails_orders1_idx` ON `book_store`.`odetails` (`ono` ASC) VISIBLE;
-- -----------------------------------------------------
-- Table `book_store`.`cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`cart` (
    `userid` INT NOT NULL,
    `isbn` CHAR(10) NOT NULL,
    `qty` INT NOT NULL,
    PRIMARY KEY (`userid`, `isbn`),
    CONSTRAINT `fk_cart_members` FOREIGN KEY (`userid`) REFERENCES `book_store`.`members` (`userid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT `fk_cart_books1` FOREIGN KEY (`isbn`) REFERENCES `book_store`.`books` (`isbn`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;
CREATE INDEX `fk_cart_members_idx` ON `book_store`.`cart` (`userid` ASC) VISIBLE;
CREATE INDEX `fk_cart_books1_idx` ON `book_store`.`cart` (`isbn` ASC) VISIBLE;
SET SQL_MODE = @OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;