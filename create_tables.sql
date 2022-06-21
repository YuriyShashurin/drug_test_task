CREATE TABLE Login(
    id serial primary key,
    login VARCHAR(50) NOT NULL ,
    password VARCHAR(30) NOT NULL,
    name VARCHAR(30) NOT NULL,
    birth Date NOT NULL,
    phone VARCHAR(12) NOT NULL,
    tg VARCHAR(50),
    email VARCHAR(50)
    );