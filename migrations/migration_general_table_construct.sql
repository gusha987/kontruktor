CREATE TABLE IF NOT EXISTS `data`.`actors` (
  `url_id` INT NOT NULL,
  `actor` VARCHAR(45) NOT NULL,
  `role` VARCHAR(45) NULL,
  PRIMARY KEY (`url_id`),
  UNIQUE INDEX `url_id_UNIQUE` (`url_id` ASC) VISIBLE);
  CREATE TABLE IF NOT EXISTS `data`.`Urls` (
  `id` INT NOT NULL,
  `url` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `url_UNIQUE` (`url` ASC) VISIBLE);