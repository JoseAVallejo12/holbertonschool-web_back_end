DROP DATABASE IF EXISTS `holberton`;
CREATE DATABASE IF NOT EXISTS `holberton`
CHARACTER SET `utf8`
COLLATE `utf8_persian_ci`;

CREATE TABLE IF NOT EXISTS `holberton`.`tableName` (
  `id` INT(12) NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL UNIQUE
  `name` VARCHAR(255),
  PRIMARY KEY (`id`)
) ENGINE = InnoDB CHARSET = utf8 COLLATE utf8_persian_ci;
