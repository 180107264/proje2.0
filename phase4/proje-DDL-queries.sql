CREATE TABLE Users(
    user_id             INTEGER     PRIMARY KEY,
    name                TEXT        NOT NULL,
    surename            TEXT        NOT NULL,
    city                TEXT        NOT NULL,
    email               TEXT        NOT NULL,
    password            TEXT        NOT NULL,
    profile_picture     BLOB
);

CREATE TABLE Admins(
    admin_id            INTEGER     PRIMARY KEY,
    name                TEXT        NOT NULL,
    surename            TEXT        NOT NULL,
    login               TEXT        NOT NULL,
    password            TEXT        NOT NULL
);

CREATE TABLE Phish_Info(
    phish_info_id       INTEGER     PRIMARY KEY,
    description         TEXT        NOT NULL,
    phish2_id           TEXT        NOT NULL
);

CREATE TABLE Phish1(
    phish1_id       INTEGER     PRIMARY KEY,
    domain          TEXT        NOT NULL,
    description     TEXT        NOT NULL,
    admin_id        TEXT        NOT NULL
);

CREATE TABLE Phish2(
    phish2_id       INTEGER     PRIMARY KEY,
    domain          TEXT        NOT NULL,
    description     TEXT        NOT NULL,
    admin_id        TEXT        NOT NULL,
    user_id         TEXT        NOT NULL
);