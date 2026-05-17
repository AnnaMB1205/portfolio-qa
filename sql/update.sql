UPDATE usuarios
SET email = 'lauratest@gmail.com' 
WHERE LOWER(name) = 'laura';
UPDATE usuarios
SET age = 21 
WHERE age = 20;
DELETE FROM usuarios 
WHERE age = 30;
DELETE FROM usuarios 
WHERE LOWER(name) = 'pedro';
