-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema book_store
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema book_store
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `book_store` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `book_store` ;

-- -----------------------------------------------------
-- Table `book_store`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`books` (
  `isbn` CHAR(10) NOT NULL,
  `author` VARCHAR(100) NOT NULL,
  `title` VARCHAR(200) NOT NULL,
  `price` FLOAT NOT NULL,
  `subject` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`isbn`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_store`.`members`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`members` (
  `fname` VARCHAR(50) NOT NULL,
  `lname` VARCHAR(50) NOT NULL,
  `address` VARCHAR(50) NOT NULL,
  `city` VARCHAR(30) NOT NULL,
  `zip` INT NOT NULL,
  `phone` VARCHAR(15) NULL DEFAULT NULL,
  `email` VARCHAR(40) NOT NULL,
  `userid` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`userid`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_store`.`cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`cart` (
  `userid` INT NOT NULL,
  `isbn` CHAR(10) NOT NULL,
  `qty` INT NOT NULL,
  PRIMARY KEY (`userid`, `isbn`),
  INDEX `fk_cart_books1_idx` (`isbn` ASC) VISIBLE,
  CONSTRAINT `fk_cart_books1`
    FOREIGN KEY (`isbn`)
    REFERENCES `book_store`.`books` (`isbn`),
  CONSTRAINT `fk_cart_members1`
    FOREIGN KEY (`userid`)
    REFERENCES `book_store`.`members` (`userid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_store`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`orders` (
  `userid` INT NOT NULL,
  `ono` INT NOT NULL AUTO_INCREMENT,
  `created` DATE NULL DEFAULT NULL,
  `shipAddress` VARCHAR(50) NULL DEFAULT NULL,
  `shipCity` VARCHAR(30) NULL DEFAULT NULL,
  `shipZip` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ono`),
  INDEX `fk_orders_members1_idx` (`userid` ASC) VISIBLE,
  CONSTRAINT `fk_orders_members1`
    FOREIGN KEY (`userid`)
    REFERENCES `book_store`.`members` (`userid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_store`.`odetails`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_store`.`odetails` (
  `ono` INT NOT NULL,
  `isbn` CHAR(10) NOT NULL,
  `qty` INT NOT NULL,
  `amount` FLOAT NOT NULL,
  PRIMARY KEY (`ono`, `isbn`),
  INDEX `fk_odetails_books1_idx` (`isbn` ASC) VISIBLE,
  CONSTRAINT `fk_odetails_books1`
    FOREIGN KEY (`isbn`)
    REFERENCES `book_store`.`books` (`isbn`),
  CONSTRAINT `fk_odetails_orders`
    FOREIGN KEY (`ono`)
    REFERENCES `book_store`.`orders` (`ono`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `test` ;

-- -----------------------------------------------------
-- Table `test`.`table1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`table1` (
  `tutorid` INT NOT NULL,
  `course_level` VARCHAR(45) NULL DEFAULT NULL,
  `course_year` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`tutorid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`table2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`table2` (
  `tutorid` INT NOT NULL,
  `course` VARCHAR(45) NOT NULL,
  `credits` VARCHAR(45) NULL DEFAULT NULL,
  `department` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`tutorid`, `course`, `department`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`table3`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`table3` (
  `department` INT NOT NULL,
  `headofdep` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`department`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `test`.`table4`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`table4` (
  `tutorid` INT NOT NULL,
  `course` VARCHAR(45) NOT NULL,
  `days` VARCHAR(45) NOT NULL,
  `students` VARCHAR(45) NULL DEFAULT NULL,
  `semester` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`tutorid`, `course`, `days`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
