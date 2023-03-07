DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS incidents;

CREATE TABLE IF NOT EXISTS users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_active SMALLINT NOT NULL DEFAULT 1,
    is_admin SMALLINT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS incidents
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_case_number TEXT NOT NULL UNIQUE,
    ip TEXT NOT NULL,
    pen_tester SMALLINT NOT NULL DEFAULT 0,
    region TEXT,
    country TEXT,
    description TEXT,
    script_injection SMALLINT NOT NULL DEFAULT 0,
    command_injection SMALLINT NOT NULL DEFAULT 0,
    sql_injection SMALLINT NOT NULL DEFAULT 0,
    cross_frame_scripting SMALLINT NOT NULL DEFAULT 0,
    path_discovery SMALLINT NOT NULL DEFAULT 0,
    cross_site_request_forgery SMALLINT NOT NULL DEFAULT 0,
    other SMALLINT NOT NULL DEFAULT 0
);

