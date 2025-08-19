
Create table if not exists students(
    id serial 
    name Text,
    email Text,
    dob Date, 
    phone Integer,
    marks Real, --real meaning we can have it as in full No--
    created_at Text,
    updated_at Text

)