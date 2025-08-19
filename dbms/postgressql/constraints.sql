
DROP TABLE IF EXISTS student_;

create table if not exists student_(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dob DATE,
    phone INTEGER NOT NULL UNIQUE,
    marks REAL CHECK(marks>-1 And marks <101),
    is_married BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
