--ensure that you can contain data--
--to ensure your data is ok
--it helps ensure the data is ok
--constraints are rules that ensure data integrity


CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,               
    admission TEXT  NOT NULL,     
    age INTEGER CHECK(age >= 0)      
    );