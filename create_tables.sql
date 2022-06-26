CREATE TABLE Profile(
    id serial primary key,
    login VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(150) NOT NULL,
    name VARCHAR(30) NOT NULL,
    birth Date NOT NULL,
    phone VARCHAR(12) NOT NULL,
    tg VARCHAR(50),
    email VARCHAR(50),
    is_authenticated BOOLEAN NOT NULL
    );