--First column keeps track  of the row number,,,should be unique

Create table if not exists students(
    id Integer primary key, Autoincrements --auto increemtn if i have new record it wil autoincrement--
    name Text,
    email Text,
    dob Text, --sqlitwe doesnt have date hence dob is a text--
    phone Integer,
    marks Real, --real meaning we can have it as in full No--
    created_at Text,
    updated_at Text


)