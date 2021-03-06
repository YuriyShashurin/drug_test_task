CREATE TABLE Profile(
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    password bytea NOT NULL,
    name VARCHAR(30) NOT NULL,
    birth Date NOT NULL,
    phone VARCHAR(12) NOT NULL,
    tg VARCHAR(50),
    email VARCHAR(50),
    is_authenticated BOOLEAN NOT NULL
    );