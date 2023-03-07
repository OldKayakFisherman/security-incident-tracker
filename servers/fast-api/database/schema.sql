CREATE TABLE users
(
    id          INTEGER NOT NULL PRIMARY KEY,
    username    TEXT    NOT NULL UNIQUE,
    full_name   TEXT    NOT NULL,
    password    TEXT    NOT NULL,
    created_at  datetime DEFAULT current_timestamp,
    modified_at datetime DEFAULT current_timestamp
);

CREATE TABLE incidents
(
   id          INTEGER NOT NULL PRIMARY KEY,
   external_case_number TEXT NOT NULL,
   ip TEXT NOT NULL,
   pen_tester BOOLEAN NOT NULL CHECK (pen_tester IN (0, 1)) DEFAULT 0,
   region  TEXT,
   country  TEXT,
   script_injection  BOOLEAN NOT NULL CHECK (script_injection IN (0, 1)) DEFAULT 0,
   command_injection BOOLEAN NOT NULL CHECK (command_injection IN (0, 1)) DEFAULT 0,
   sql_injection  BOOLEAN NOT NULL CHECK (sql_injection IN (0, 1)) DEFAULT 0,
   cross_frame_scripting  BOOLEAN NOT NULL CHECK (cross_frame_scripting IN (0, 1)) DEFAULT 0,
   path_discovery  BOOLEAN NOT NULL CHECK (path_discovery IN (0, 1)) DEFAULT 0,
   other  BOOLEAN NOT NULL CHECK (other IN (0, 1)) DEFAULT 0
);





