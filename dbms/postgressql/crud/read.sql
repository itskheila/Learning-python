---select *from student

--*aessterics higlights all columns
-- use email, name to select wanted columns

--SELECT * from student_
select name, email, phone from student_
--WHERE email = 'jane@gmail.com'
--OR
--email = 'john@gmail.com'
--OR
--phone = '123456777'

order by name asc
LIMIT 2  --LIMITS NEEDED/wanted data by 2