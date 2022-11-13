CREATE DATABASE auth;

CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'senha_forte';
GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    pwd VARCHAR(64),
    
    CONSTRAINT user_PK PRIMARY KEY (id)
) ENGINE = INNODB;

INSERT INTO
    user (email, pwd)
VALUES
    ('admin@email.com', MD5('senha_admin'));
