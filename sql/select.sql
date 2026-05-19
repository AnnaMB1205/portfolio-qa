create table usuarios (
  id SERIAL PRIMARY KEY,
  name VARCHAR, 
  email VARCHAR NOT NULL,
  subject VARCHAR NOT NULL,
  age INTEGER CHECK (age > 18),
  message VARCHAR(500) NOT NULL 
);
